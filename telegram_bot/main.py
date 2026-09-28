"""
main.py
───────
Entry point for CAT 2026 Daily Master Mentor Telegram Bot.
Includes background HTTP server for Render/cloud deployment and port health checks.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import logging
import asyncio
import os
from telegram.ext import Application
from telegram.request import HTTPXRequest

import config
from handlers import register_handlers
from scheduler import register_jobs
import server

logging.basicConfig(
    format  = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    level   = logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

logger = logging.getLogger("cat_bot_main")

def main() -> None:
    logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    logger.info("  CAT 2026 Daily Master Mentor Bot   ")
    logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    logger.info("Bot Token: ...%s", config.BOT_TOKEN[-8:] if config.BOT_TOKEN else "MISSING")
    logger.info("Chat ID: %s", config.CHAT_ID)
    logger.info("Model: %s", config.GEMINI_MODEL)
    logger.info("Master sets dir: %s", config.DAILY_SETS_DIR)
    logger.info("Morning schedule: %02d:%02d IST", config.SCHEDULE_MORNING_HOUR, config.SCHEDULE_MORNING_MIN)
    logger.info("Evening schedule: %02d:%02d IST", config.SCHEDULE_EVENING_HOUR, config.SCHEDULE_EVENING_MIN)

    if not config.BOT_TOKEN:
        logger.error("BOT_TOKEN is missing! Please check .env file.")
        sys.exit(1)

    # Start Flask background health-check server (needed for Render port binding)
    server.start_server()

    # Build Application with custom timeouts and JobQueue
    req = HTTPXRequest(connect_timeout=25.0, read_timeout=25.0)
    app = (
        Application.builder()
        .token(config.BOT_TOKEN)
        .request(req)
        .build()
    )

    register_handlers(app)
    logger.info("All command & callback handlers registered")

    register_jobs(app)
    logger.info("Scheduled morning & evening jobs registered")

    logger.info("Bot is active — starting polling loop...")
    logger.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app.run_polling(
        poll_interval        = 1,
        timeout              = 20,
        drop_pending_updates = True,
    )

if __name__ == "__main__":
    main()