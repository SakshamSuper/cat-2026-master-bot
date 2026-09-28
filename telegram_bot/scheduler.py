"""
scheduler.py
────────────
Automated morning dispatch and evening check-in jobs for CAT Preparation Bot.
Delivers the latest updated CAT 2026 Enhanced Master Plan every morning at 08:00 AM IST.
"""

import logging
from datetime import time
from telegram.ext import Application, ContextTypes
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import config
import tracker
import parser
import master_plan
from handlers import send_safe_text, get_day_markup

logger = logging.getLogger("scheduler")

async def morning_dispatch_job(context: ContextTypes.DEFAULT_TYPE):
    """08:00 AM IST Morning Delivery of Today's Brand New CAT Master Set."""
    chat_id = config.CHAT_ID
    if not chat_id:
        logger.warning("No CHAT_ID configured for morning dispatch.")
        return

    # Automatically advances to the next consecutive day every morning
    active_day = tracker.prepare_morning_dispatch_day()
    logger.info("Running morning dispatch for Day %d to chat %s", active_day, chat_id)

    # Check if Day file exists; if not, generate via Gemini Master Plan engine
    file_path = parser.get_day_file(active_day)
    if not file_path:
        logger.info("Day %d set not found. Auto-generating brand new set using Gemini Master Blueprint...", active_day)
        try:
            file_path = master_plan.generate_next_set(active_day)
        except Exception as e:
            logger.error("Auto-generation failed for Day %d: %s", active_day, e)

    data = parser.parse_day_set(active_day)
    if "error" in data:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"🌅 *Good Morning Saksham!* Today is target **Day {active_day}**, but set could not be loaded.\nUse `/day` to select a set."
        )
        return

    has_boosters = bool(data.get("boosters"))
    booster_summary = ""
    if has_boosters:
        # Extract formula / shortcut titles if possible
        booster_summary = (
            "✨ *Today's Section 0 Daily Boosters Included:*\n"
            "• 📐 Formula of the Day\n"
            "• ⚡ Shortcut of the Day\n"
            "• 🧮 60-Second Speed Drill (5 Problems)\n"
            "• 📖 5 CAT RC Vocabulary Words\n"
            "• 🧠 Concept & Trap Analysis\n\n"
        )

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

    await send_safe_text(context, chat_id, greeting, reply_markup=get_day_markup(active_day))

    # Send document attachment
    if file_path and file_path.exists():
        try:
            with open(file_path, "rb") as f:
                await context.bot.send_document(
                    chat_id=chat_id,
                    document=f,
                    filename=file_path.name,
                    caption=f"📄 Day {active_day} Master Set Complete Document"
                )
        except Exception as e:
            logger.error("Failed to attach morning file: %s", e)


async def evening_checkin_job(context: ContextTypes.DEFAULT_TYPE):
    """20:00 PM IST Evening Accountability and Solutions drop."""
    chat_id = config.CHAT_ID
    if not chat_id:
        return

    active_day = tracker.get_active_day()
    logger.info("Running evening check-in for Day %d to chat %s", active_day, chat_id)

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
    await send_safe_text(context, chat_id, msg, reply_markup=markup)


def register_jobs(app: Application):
    """Registers the daily morning and evening jobs with JobQueue."""
    jq = app.job_queue
    if jq is None:
        logger.warning("JobQueue is not installed or available.")
        return

    # Morning job: 08:00 AM IST
    morning_time = time(
        hour=config.SCHEDULE_MORNING_HOUR,
        minute=config.SCHEDULE_MORNING_MIN,
        tzinfo=config.TIMEZONE
    )
    jq.run_daily(
        morning_dispatch_job,
        time=morning_time,
        name="cat_morning_dispatch"
    )
    logger.info("Morning dispatch scheduled for %02d:%02d IST", config.SCHEDULE_MORNING_HOUR, config.SCHEDULE_MORNING_MIN)

    # Evening job: 20:00 PM IST
    evening_time = time(
        hour=config.SCHEDULE_EVENING_HOUR,
        minute=config.SCHEDULE_EVENING_MIN,
        tzinfo=config.TIMEZONE
    )
    jq.run_daily(
        evening_checkin_job,
        time=evening_time,
        name="cat_evening_checkin"
    )
    logger.info("Evening check-in scheduled for %02d:%02d IST", config.SCHEDULE_EVENING_HOUR, config.SCHEDULE_EVENING_MIN)