"""
tracker.py
──────────
Handles study progress, streak tracking, and automatic daily progression.
Guarantees a brand-new day set is selected each morning based on calendar progression.
"""

import json
import re
from datetime import datetime, date, timedelta
from pathlib import Path
import config

START_DATE = date(2026, 9, 29)
BASE_DAY = 1

def _default_state() -> dict:
    return {
        "active_day": None,
        "completed_days": [],
        "streak": 0,
        "last_completed_date": None,
        "last_dispatched_date": None,
        "last_dispatched_day": None,
        "manual_active_day": None,
        "scores": {}
    }

def load_progress() -> dict:
    if not config.PROGRESS_FILE.exists():
        state = _default_state()
        save_progress(state)
        return state
    try:
        with open(config.PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return _default_state()

def save_progress(data: dict) -> None:
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(config.PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def calculate_calendar_day() -> int:
    """Calculates what day it should be based on calendar days elapsed since launch."""
    today = date.today()
    days_elapsed = (today - START_DATE).days
    return max(1, BASE_DAY + days_elapsed)

def get_active_day() -> int:
    data = load_progress()
    if data.get("manual_active_day") is not None:
        return data["manual_active_day"]
    return calculate_calendar_day()

def set_active_day(day_num: int) -> int:
    data = load_progress()
    data["manual_active_day"] = day_num
    save_progress(data)
    return day_num

def prepare_morning_dispatch_day() -> int:
    """Returns today's new day number for morning dispatch, guaranteed to advance daily."""
    data = load_progress()
    today_str = date.today().isoformat()

    if data.get("manual_active_day") is not None:
        last_disp_date = data.get("last_dispatched_date")
        if last_disp_date and last_disp_date != today_str:
            data["manual_active_day"] += 1
        day = data["manual_active_day"]
    else:
        # Guaranteed fresh new day every single calendar morning!
        day = calculate_calendar_day()

    data["last_dispatched_date"] = today_str
    data["last_dispatched_day"] = day
    data["active_day"] = day
    save_progress(data)
    return day

def mark_completed(day_num: int, score_notes: str = None) -> dict:
    data = load_progress()
    today_str = date.today().isoformat()

    if day_num not in data["completed_days"]:
        data["completed_days"].append(day_num)
        data["completed_days"].sort()

    last_date_str = data.get("last_completed_date")
    if last_date_str:
        try:
            last_date = date.fromisoformat(last_date_str)
            if last_date == date.today():
                pass
            elif last_date == date.today() - timedelta(days=1):
                data["streak"] = data.get("streak", 0) + 1
            else:
                data["streak"] = 1
        except Exception:
            data["streak"] = 1
    else:
        data["streak"] = 1

    data["last_completed_date"] = today_str

    if score_notes:
        data.setdefault("scores", {})[str(day_num)] = score_notes

    # Advance manual active day if user was tracking manual active day
    if data.get("manual_active_day") == day_num:
        data["manual_active_day"] = day_num + 1

    save_progress(data)
    _sync_readme(day_num)
    return data

def _sync_readme(day_num: int) -> None:
    if not config.README_PATH.exists():
        return
    try:
        content = config.README_PATH.read_text(encoding="utf-8")
        pattern = rf"(\| Day {day_num} \|.*?\|\s*)⬜ Pending(\s*\|)"
        new_content = re.sub(pattern, r"\1✅ Completed\2", content)
        if new_content != content:
            config.README_PATH.write_text(new_content, encoding="utf-8")
    except Exception as e:
        print(f"Warning: Failed to sync README.md: {e}")

def get_stats_summary() -> str:
    data = load_progress()
    total_days = 65
    completed_count = len(data.get("completed_days", []))
    remaining = max(0, total_days - completed_count)
    streak = data.get("streak", 0)
    active_day = get_active_day()
    pct = (completed_count / total_days) * 100 if total_days > 0 else 0

    bar_len = 10
    filled = int(round(bar_len * (completed_count / total_days))) if total_days > 0 else 0
    bar = "▓" * filled + "░" * (bar_len - filled)

    msg = (
        f"📊 *CAT 2026 Preparation Progress*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 *Active Day Target:* Day {active_day}\n"
        f"🔥 *Daily Streak:* {streak} day{'s' if streak != 1 else ''}\n"
        f"✅ *Completed Sets:* {completed_count}/{total_days} ({pct:.1f}%)\n"
        f"⏳ *Remaining Sets:* {remaining} days\n"
        f"📈 *Progress:* `[{bar}]`\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💡 Use `/done <day>` after solving to mark completion."
    )
    return msg