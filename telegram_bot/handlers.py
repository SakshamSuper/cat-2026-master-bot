"""
handlers.py
───────────
Telegram message and callback handlers for CAT Preparation Bot.
Supports Enhanced CAT 2026 Master Plan format (Section 0 Boosters, Section 1 QA,
Section 2 DILR, Section 3 VARC, Section 4 Solutions), Shortcut Bible, and Syllabus Reference.
"""

import logging
from pathlib import Path
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler

import config
import tracker
import parser
import ai_tutor
import master_plan

logger = logging.getLogger("handlers")

async def send_safe_text(context: ContextTypes.DEFAULT_TYPE, chat_id: int, text: str, reply_markup=None):
    """Sends text safely, falling back to plain text if Telegram Markdown parsing fails."""
    chunks = parser.chunk_text(text, max_chars=3800)
    for i, chunk in enumerate(chunks):
        markup = reply_markup if i == len(chunks) - 1 else None
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=chunk,
                parse_mode="Markdown",
                reply_markup=markup,
                disable_web_page_preview=True
            )
        except Exception:
            await context.bot.send_message(
                chat_id=chat_id,
                text=chunk,
                parse_mode=None,
                reply_markup=markup,
                disable_web_page_preview=True
            )

def get_day_markup(day_num: int) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("⚡ Section 0: Boosters", callback_data=f"sec_boost_{day_num}"),
            InlineKeyboardButton("📐 Section 1: QA", callback_data=f"sec_qa_{day_num}"),
        ],
        [
            InlineKeyboardButton("🧩 Section 2: DILR", callback_data=f"sec_dilr_{day_num}"),
            InlineKeyboardButton("📖 Section 3: VARC", callback_data=f"sec_varc_{day_num}"),
        ],
        [
            InlineKeyboardButton("💡 Detailed Solutions", callback_data=f"sec_sol_{day_num}"),
            InlineKeyboardButton("📄 Send File (.md)", callback_data=f"sec_file_{day_num}"),
        ],
        [
            InlineKeyboardButton("📚 Shortcut Bible", callback_data="cmd_shortcuts"),
            InlineKeyboardButton("🎯 Master Plan", callback_data="cmd_plan"),
        ],
        [
            InlineKeyboardButton("✅ Mark Done", callback_data=f"sec_done_{day_num}"),
            InlineKeyboardButton("📊 My Stats", callback_data="cmd_stats"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name if update.effective_user else "Aspirant"
    active_day = tracker.get_active_day()
    msg = (
        f"🎯 *Welcome {user_name} to CAT 2026 Master Mentor!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Delivering the latest updated *CAT 2026 Enhanced Master Plan* every morning.\n\n"
        f"📌 *Active Target:* Day {active_day}\n\n"
        f"🚀 *Quick Commands:*\n"
        f"• `/today` — Today's Master Set & Interactive Menu\n"
        f"• `/boosters` — Today's Formula, Shortcut, Speed Drill & Vocab\n"
        f"• `/qa`, `/dilr`, `/varc` — Drill individual sections\n"
        f"• `/solutions` — Complete step-by-step methods & traps\n"
        f"• `/shortcuts` — Open the 60-Day CAT Shortcut & Accuracy Bible\n"
        f"• `/syllabus` — View the CAT 2026 Topic Syllabus Reference\n"
        f"• `/plan` — CAT 2026 99+ Percentile Master Blueprint\n"
        f"• `/file` — Download today's complete `.md` document\n"
        f"• `/done` — Mark today completed & increase streak\n"
        f"• `/stats` — Check your preparation dashboard\n"
        f"• `/drill <topic>` — 3-Question topic speed drill\n"
        f"• `/ask <doubt>` — Ask Gemini CAT Mentor any question\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Tap `/today` or `/boosters` to begin!"
    )
    await send_safe_text(context, update.effective_chat.id, msg)

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, context)

async def cmd_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = tracker.get_active_day()
    await send_day_card(context, update.effective_chat.id, day_num)

async def cmd_day(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and context.args[0].isdigit():
        day_num = int(context.args[0])
    else:
        day_num = tracker.get_active_day()
    await send_day_card(context, update.effective_chat.id, day_num)

async def send_day_card(context: ContextTypes.DEFAULT_TYPE, chat_id: int, day_num: int):
    data = parser.parse_day_set(day_num)
    if "error" in data:
        await context.bot.send_message(chat_id=chat_id, text=f"⚠️ {data['error']}")
        return

    overview_snippet = data["overview"]
    if len(overview_snippet) > 600:
        overview_snippet = overview_snippet[:600] + "..."

    # If boosters are present, show a quick teaser
    has_boosters = bool(data.get("boosters"))
    booster_note = "Includes: 📐 Formula · ⚡ Shortcut · 🧮 Speed Drill · 📖 5 Vocab Words · 🧠 Exam Trap Analysis\n\n" if has_boosters else ""

    msg = (
        f"☀️ *CAT 2026 Enhanced Master Set — Day {day_num}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{overview_snippet}\n\n"
        f"{booster_note}"
        f"⚡ Tap a section below to start practicing:"
    )
    await send_safe_text(context, chat_id, msg, reply_markup=get_day_markup(day_num))

async def cmd_boosters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = int(context.args[0]) if context.args and context.args[0].isdigit() else tracker.get_active_day()
    data = parser.parse_day_set(day_num)
    if not data.get("boosters"):
        await send_safe_text(context, update.effective_chat.id, f"⚠️ Section 0 Boosters for Day {day_num} not found.")
        return
    await send_safe_text(context, update.effective_chat.id, data["boosters"])

async def cmd_qa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = int(context.args[0]) if context.args and context.args[0].isdigit() else tracker.get_active_day()
    data = parser.parse_day_set(day_num)
    if not data.get("qa"):
        await send_safe_text(context, update.effective_chat.id, f"⚠️ Section 1 (QA) for Day {day_num} not found.")
        return
    await send_safe_text(context, update.effective_chat.id, data["qa"])

async def cmd_dilr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = int(context.args[0]) if context.args and context.args[0].isdigit() else tracker.get_active_day()
    data = parser.parse_day_set(day_num)
    if not data.get("dilr"):
        await send_safe_text(context, update.effective_chat.id, f"⚠️ Section 2 (DILR) for Day {day_num} not found.")
        return
    await send_safe_text(context, update.effective_chat.id, data["dilr"])

async def cmd_varc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = int(context.args[0]) if context.args and context.args[0].isdigit() else tracker.get_active_day()
    data = parser.parse_day_set(day_num)
    if not data.get("varc"):
        await send_safe_text(context, update.effective_chat.id, f"⚠️ Section 3 (VARC) for Day {day_num} not found.")
        return
    await send_safe_text(context, update.effective_chat.id, data["varc"])

async def cmd_solutions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = int(context.args[0]) if context.args and context.args[0].isdigit() else tracker.get_active_day()
    data = parser.parse_day_set(day_num)
    if not data.get("solutions"):
        await send_safe_text(context, update.effective_chat.id, f"⚠️ Detailed solutions for Day {day_num} not found.")
        return
    await send_safe_text(context, update.effective_chat.id, f"💡 *Day {day_num} — Solutions & Strategy Analysis*\n\n{data['solutions']}")

async def cmd_shortcuts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bible_path = config.CAT_PREP_DIR / "CAT2026_Shortcut_Bible.md"
    if not bible_path.exists():
        await send_safe_text(context, update.effective_chat.id, "⚠️ Shortcut Bible document not found.")
        return
    with open(bible_path, "rb") as f:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=f,
            filename="CAT2026_Shortcut_Bible.md",
            caption="⚡ CAT 2026 — Master Shortcut & Accuracy Bible (60-Day Sprint)"
        )

async def cmd_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    syl_path = config.CAT_PREP_DIR / "CAT2026_Syllabus_Reference.md"
    if not syl_path.exists():
        await send_safe_text(context, update.effective_chat.id, "⚠️ Syllabus document not found.")
        return
    with open(syl_path, "rb") as f:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=f,
            filename="CAT2026_Syllabus_Reference.md",
            caption="🎯 CAT 2026 Official Syllabus & Weightage Reference"
        )

async def cmd_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = int(context.args[0]) if context.args and context.args[0].isdigit() else tracker.get_active_day()
    file_path = parser.get_day_file(day_num)
    if not file_path:
        await send_safe_text(context, update.effective_chat.id, f"⚠️ Day {day_num} file not found.")
        return
    with open(file_path, "rb") as f:
        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=f,
            filename=file_path.name,
            caption=f"📄 Day {day_num} Complete Master Set"
        )

async def cmd_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day_num = int(context.args[0]) if context.args and context.args[0].isdigit() else tracker.get_active_day()
    state = tracker.mark_completed(day_num)
    msg = (
        f"🎉 *Day {day_num} Marked Complete!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🔥 Daily Streak: *{state['streak']} days*\n"
        f"🎯 Next Target: *Day {state['active_day']}*\n\n"
        f"Keep going! Consistency is how 99+ percentiles are built."
    )
    await send_safe_text(context, update.effective_chat.id, msg)

async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = tracker.get_stats_summary()
    await send_safe_text(context, update.effective_chat.id, msg)

async def cmd_setday(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await send_safe_text(context, update.effective_chat.id, "Usage: `/setday <number>` (e.g. `/setday 1` or `/setday 36`)")
        return
    num = int(context.args[0])
    tracker.set_active_day(num)
    await send_safe_text(context, update.effective_chat.id, f"🎯 Active target day updated to **Day {num}**.")

async def cmd_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = master_plan.get_master_plan()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg,
        parse_mode="HTML"
    )

async def cmd_ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await send_safe_text(context, update.effective_chat.id, "Usage: `/ask <your question or doubt>`")
        return
    query = " ".join(context.args)
    active_day = tracker.get_active_day()
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    ans = ai_tutor.answer_doubt(query, current_day=active_day)
    await send_safe_text(context, update.effective_chat.id, f"🤖 *Gemini CAT Mentor:*\n\n{ans}")

async def cmd_drill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await send_safe_text(context, update.effective_chat.id, "Usage: `/drill <topic>` (e.g. `/drill Remainders` or `/drill Para Jumbles`)")
        return
    topic = " ".join(context.args)
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    drill_text = ai_tutor.generate_topic_drill(topic)
    await send_safe_text(context, update.effective_chat.id, f"⚡ *Topic Drill: {topic}*\n━━━━━━━━━━━━━━━━━━━━\n\n{drill_text}")

async def on_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    chat_id = query.message.chat_id

    if data.startswith("sec_boost_"):
        day = int(data.split("_")[2])
        p_data = parser.parse_day_set(day)
        await send_safe_text(context, chat_id, p_data.get("boosters", "Section 0 Boosters not found."))
    elif data.startswith("sec_qa_"):
        day = int(data.split("_")[2])
        p_data = parser.parse_day_set(day)
        await send_safe_text(context, chat_id, p_data.get("qa", "QA section not found."))
    elif data.startswith("sec_dilr_"):
        day = int(data.split("_")[2])
        p_data = parser.parse_day_set(day)
        await send_safe_text(context, chat_id, p_data.get("dilr", "DILR section not found."))
    elif data.startswith("sec_varc_"):
        day = int(data.split("_")[2])
        p_data = parser.parse_day_set(day)
        await send_safe_text(context, chat_id, p_data.get("varc", "VARC section not found."))
    elif data.startswith("sec_sol_"):
        day = int(data.split("_")[2])
        p_data = parser.parse_day_set(day)
        await send_safe_text(context, chat_id, f"💡 *Day {day} Solutions:*\n\n" + p_data.get("solutions", "Solutions not found."))
    elif data.startswith("sec_file_"):
        day = int(data.split("_")[2])
        file_path = parser.get_day_file(day)
        if file_path:
            with open(file_path, "rb") as f:
                await context.bot.send_document(
                    chat_id=chat_id,
                    document=f,
                    filename=file_path.name,
                    caption=f"📄 Day {day} Complete Master Set"
                )
    elif data == "cmd_shortcuts":
        await cmd_shortcuts(update, context)
    elif data == "cmd_plan":
        await cmd_plan(update, context)
    elif data.startswith("sec_done_"):
        day = int(data.split("_")[2])
        state = tracker.mark_completed(day)
        await send_safe_text(context, chat_id, f"🎉 *Day {day} Marked Done!*\nStreak: {state['streak']} days 🔥 | Next: Day {state['active_day']}")
    elif data == "cmd_stats":
        await send_safe_text(context, chat_id, tracker.get_stats_summary())

def register_handlers(app):
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("today", cmd_today))
    app.add_handler(CommandHandler("day", cmd_day))
    app.add_handler(CommandHandler("boosters", cmd_boosters))
    app.add_handler(CommandHandler("qa", cmd_qa))
    app.add_handler(CommandHandler("dilr", cmd_dilr))
    app.add_handler(CommandHandler("varc", cmd_varc))
    app.add_handler(CommandHandler("solutions", cmd_solutions))
    app.add_handler(CommandHandler("shortcuts", cmd_shortcuts))
    app.add_handler(CommandHandler("syllabus", cmd_syllabus))
    app.add_handler(CommandHandler("file", cmd_file))
    app.add_handler(CommandHandler("done", cmd_done))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("setday", cmd_setday))
    app.add_handler(CommandHandler("plan", cmd_plan))
    app.add_handler(CommandHandler("ask", cmd_ask))
    app.add_handler(CommandHandler("drill", cmd_drill))
    app.add_handler(CallbackQueryHandler(on_callback_query))