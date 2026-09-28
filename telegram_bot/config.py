"""
config.py
─────────
Configuration and path resolutions for CAT Preparation Telegram Bot.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import pytz

# Bot root and CAT prep repository paths
BOT_DIR = Path(__file__).resolve().parent
load_dotenv(BOT_DIR / ".env")

CAT_PREP_DIR = BOT_DIR.parent
DAILY_SETS_DIR = CAT_PREP_DIR / "Daily_Master_Sets"
README_PATH = CAT_PREP_DIR / "README.md"

DATA_DIR = BOT_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
PROGRESS_FILE = DATA_DIR / "progress.json"

# Telegram credentials
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
chat_id_raw = os.getenv("CHAT_ID", "").strip()
CHAT_ID = int(chat_id_raw) if chat_id_raw else None

# Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()

# Scheduler Settings (Asia/Kolkata)
TIMEZONE = pytz.timezone("Asia/Kolkata")
SCHEDULE_MORNING_HOUR = int(os.getenv("SCHEDULE_MORNING_HOUR", "8"))
SCHEDULE_MORNING_MIN = int(os.getenv("SCHEDULE_MORNING_MIN", "0"))
SCHEDULE_EVENING_HOUR = int(os.getenv("SCHEDULE_EVENING_HOUR", "20"))
SCHEDULE_EVENING_MIN = int(os.getenv("SCHEDULE_EVENING_MIN", "0"))

DEFAULT_START_DAY = int(os.getenv("DEFAULT_START_DAY", "34"))
