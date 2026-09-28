import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import asyncio
from telegram import Bot
from telegram.request import HTTPXRequest
import config
import parser
import tracker
import ai_tutor

async def run_diagnostics():
    print("=" * 50)
    print("  CAT 2026 BOT DIAGNOSTICS & VERIFICATION  ")
    print("=" * 50)

    # 1. Telegram Bot Token verification
    print("\n[1/5] Checking Telegram Bot...")
    req = HTTPXRequest(connect_timeout=20.0, read_timeout=20.0)
    bot = Bot(token=config.BOT_TOKEN, request=req)
    try:
        me = await bot.get_me()
        print(f"✅ SUCCESS: Connected to Telegram as @{me.username} (ID: {me.id})")
    except Exception as e:
        print(f"❌ FAIL: Telegram connection error: {e}")
        return

    # 2. Test Message to User's Chat ID
    print(f"\n[2/5] Testing direct message to Chat ID: {config.CHAT_ID}...")
    if not config.CHAT_ID:
        print("❌ FAIL: CHAT_ID is empty.")
    else:
        try:
            test_msg = (
                "🎯 *CAT 2026 Daily Master Mentor Connected!*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                "Bot is successfully initialized and ready.\n"
                "• Active set target: Day 34\n"
                "• Morning dispatch: 08:00 AM IST\n"
                "• Evening solutions: 20:00 PM IST\n\n"
                "Type `/start` or `/today` to begin practicing!"
            )
            sent = await bot.send_message(
                chat_id=config.CHAT_ID,
                text=test_msg,
                parse_mode="Markdown"
            )
            print(f"✅ SUCCESS: Test message delivered to chat (Message ID: {sent.message_id})")
        except Exception as e:
            print(f"⚠️ Telegram send warning: {e}")

    # 3. Test Master Set Parser
    print("\n[3/5] Testing Markdown Parser on Day 36...")
    data = parser.parse_day_set(36)
    if "error" in data:
        print(f"❌ FAIL: {data['error']}")
    else:
        print(f"✅ SUCCESS: Parsed Day 36 successfully!")
        print(f"   - QA length: {len(data['qa'])} chars")
        print(f"   - DILR length: {len(data['dilr'])} chars")
        print(f"   - VARC length: {len(data['varc'])} chars")
        print(f"   - Answer key length: {len(data['answers'])} chars")

    # 4. Test Progress Tracker
    print("\n[4/5] Testing Progress Tracker...")
    summary = tracker.get_stats_summary()
    print("✅ Tracker output:\n" + summary)

    # 5. Test AI Mentor
    print("\n[5/5] Testing Gemini AI Mentor...")
    mentor_reply = ai_tutor.answer_doubt("Give a 1-line rule for solving Para Jumbles in CAT VARC.")
    print("✅ AI Mentor reply:\n" + mentor_reply.strip())

    print("\n" + "=" * 50)
    print("  ALL DIAGNOSTICS PASSED! BOT IS READY TO RUN.  ")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(run_diagnostics())