"""
tracker.py
──────────
Handles study progress, streak tracking, and synchronization with README.md.
"""

import json
import re
from datetime import datetime, date, timedelta
from pathlib import Path
import config

def _default_state() -> dict:
    return {
        "active_day": config.DEFAULT_START_DAY,
        "completed_days": [],
        "streak": 0,
        "last_completed_date": None,
        "last_dispatched_date": None,
        "last_dispatched_day": None,
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
    with open(config.PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_active_day() -> int:
    return load_progress().get("active_day", config.DEFAULT_START_DAY)

def set_active_day(day_num: int) -> int:
    data = load_progress()
    data["active_day"] = day_num
    save_progress(data)
    return day_num

def prepare_morning_dispatch_day() -> int:
    """Prepares and returns the day number for morning dispatch, auto-advancing to the next day each morning."""
    data = load_progress()
    today_str = date.today().isoformat()
    last_disp_date = data.get("last_dispatched_date")
    active_day = data.get("active_day", config.DEFAULT_START_DAY)

    # If this is a new calendar day and we already dispatched on a previous date
    if last_disp_date and last_disp_date != today_str:
        active_day += 1
        data["active_day"] = active_day

    data["last_dispatched_date"] = today_str
    data["last_dispatched_day"] = active_day
    save_progress(data)
    return active_day

def mark_completed(day_num: int, score_notes: str = None) -> dict:
    data = load_progress()
    today_str = date.today().isoformat()

    if day_num not in data["completed_days"]:
        data["completed_days"].append(day_num)
        data["completed_days"].sort()

    # Update streak
    last_date_str = data.get("last_completed_date")
    if last_date_str:
        try:
            last_date = date.fromisoformat(last_date_str)
            if last_date == date.today():
                pass # Already completed today
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

    # Advance active day if user finished active day
    if data["active_day"] == day_num:
        data["active_day"] = day_num + 1

    save_progress(data)
    _sync_readme(day_num)
    return data

def _sync_readme(day_num: int) -> None:
    if not config.README_PATH.exists():
        return
    try:
        content = config.README_PATH.read_text(encoding="utf-8")
        # Replace ⬜ Pending with ✅ Completed for Day X
        pattern = rf"(\| Day {day_num} \|.*?\|\s*)⬜ Pending(\s*\|)"
        new_content = re.sub(pattern, r"\1✅ Completed\2", content)
        if new_content != content:
            config.README_PATH.write_text(new_content, encoding="utf-8")
    except Exception as e:
        print(f"Warning: Failed to sync README.md: {e}")

def get_stats_summary() -> str:
    data = load_progress()
    total_days = 65  # Base Day 34 to Day 98
    completed_count = len(data.get("completed_days", []))
    remaining = max(0, total_days - completed_count)
    streak = data.get("streak", 0)
    active_day = data.get("active_day", config.DEFAULT_START_DAY)
    pct = (completed_count / total_days) * 100 if total_days > 0 else 0

    bar_len = 10
    filled = int(round(bar_len * (completed_count / total_days))) if total_days > 0 else 0
    bar = "▓" * filled + "░" * (bar_len - filled)

    msg = (
        f"📊 *CAT 2026 Preparation Progress*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 *Active Target:* Day {active_day}\n"
        f"🔥 *Daily Streak:* {streak} day{'s' if streak != 1 else ''}\n"
        f"✅ *Completed Sets:* {completed_count}/{total_days} ({pct:.1f}%)\n"
        f"⏳ *Remaining Base Sets:* {remaining} days\n"
        f"📈 *Progress:* `[{bar}]`\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💡 Use `/done <day>` after solving to mark completion."
    )
    return msg