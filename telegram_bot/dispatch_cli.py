"""
dispatch_cli.py
───────────────
Standalone one-shot CLI runner for automated morning/evening dispatches.
Used by GitHub Actions / cloud cron jobs without keeping a process alive.
"""

import sys
import os
from pathlib import Path
import asyncio
from telegram import Bot
from telegram.request import HTTPXRequest

BOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(BOT_DIR))

import config
import tracker
import parser
import master_plan
from handlers import send_safe_text, get_day_markup

async def run_morning():
    print("Executing one-shot morning dispatch...")
    if not config.BOT_TOKEN or not config.CHAT_ID:
        print("Error: BOT_TOKEN or CHAT_ID not set.")
        sys.exit(1)

    req = HTTPXRequest(connect_timeout=20.0, read_timeout=20.0)
    bot = Bot(token=config.BOT_TOKEN, request=req)

    # Class to mimic ContextTypes.DEFAULT_TYPE
    class MockContext:
        def __init__(self, b):
            self.bot = b

    ctx = MockContext(bot)
    active_day = tracker.prepare_morning_dispatch_day()
    print(f"Target day for morning: Day {active_day}")

    file_path = parser.get_day_file(active_day)
    if not file_path:
        print(f"Generating new set for Day {active_day}...")
        file_path = master_plan.generate_next_set(active_day)

    data = parser.parse_day_set(active_day)
    has_boosters = bool(data.get("boosters"))
    booster_summary = (
        "✨ *Today's Section 0 Daily Boosters Included:*\n"
        "• 📐 Formula of the Day\n"
        "• ⚡ Shortcut of the Day\n"
        "• 🧮 60-Second Speed Drill (5 Problems)\n"
        "• 📖 5 CAT RC Vocabulary Words\n"
        "• 🧠 Concept & Trap Analysis\n\n"
    ) if has_boosters else ""

    greeting = (
        f"☀️ *Good Morning Saksham! CAT 2026 Master Set — Day {active_day}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 *Target:* 99+ Percentile Track | 60-Day Sprint\n\n"
        f"{booster_summary}"
        f"• Section 1: Quantitative Aptitude (28 Qs)\n"
        f"• Section 2: DILR (4 Complete Sets, 16 Qs)\n"
        f"• Section 3: VARC (2 Full RCs + 6 VA Qs)\n\n"
        f"⚡ Tap below to practice or open the attached document:"
    )

    await send_safe_text(ctx, config.CHAT_ID, greeting, reply_markup=get_day_markup(active_day))

    if file_path and file_path.exists():
        with open(file_path, "rb") as f:
            await bot.send_document(
                chat_id=config.CHAT_ID,
                document=f,
                filename=file_path.name,
                caption=f"📄 Day {active_day} Complete Master Set"
            )
    print("Morning dispatch complete!")

async def run_evening():
    print("Executing one-shot evening check-in...")
    if not config.BOT_TOKEN or not config.CHAT_ID:
        sys.exit(1)

    req = HTTPXRequest(connect_timeout=20.0, read_timeout=20.0)
    bot = Bot(token=config.BOT_TOKEN, request=req)

    class MockContext:
        def __init__(self, b):
            self.bot = b

    ctx = MockContext(bot)
    active_day = tracker.get_active_day()
    
    from telegram import InlineKeyboardMarkup, InlineKeyboardButton
    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💡 Detailed Solutions", callback_data=f"sec_sol_{active_day}"),
            InlineKeyboardButton("📚 Shortcut Bible", callback_data="cmd_shortcuts"),
        ],
        [
            InlineKeyboardButton("✅ Mark Done", callback_data=f"sec_done_{active_day}"),
            InlineKeyboardButton("📊 My Stats", callback_data="cmd_stats"),
        ]
    ])

    msg = (
        f"🌙 *Evening Review & Accountability — Day {active_day}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Did you complete today's CAT session?\n\n"
        f"1. Review step-by-step solutions, fastest CAT methods, and traps.\n"
        f"2. Add any new shortcuts to your mental reflex.\n"
        f"3. Tap **Mark Done** to lock in your daily streak!\n\n"
        f"Ask doubts anytime with `/ask <doubt>`."
    )
    await send_safe_text(ctx, config.CHAT_ID, msg, reply_markup=markup)
    print("Evening check-in complete!")

if __name__ == "__main__":
    action = sys.argv[1].lower() if len(sys.argv) > 1 else "morning"
    if action == "morning":
        asyncio.run(run_morning())
    elif action == "evening":
        asyncio.run(run_evening())
    else:
        print(f"Unknown action: {action}. Use 'morning' or 'evening'.")