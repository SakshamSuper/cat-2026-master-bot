"""
master_plan.py
──────────────
CAT 2026 Master Plan Strategy & Generation Engine.
Based on the Enhanced CAT 2026 Master Instructions created in Antigravity:
Includes Section 0 Boosters (Formula, Shortcut, Speed Drill, Vocab, Concept),
Section 1 QA (28 Qs), Section 2 DILR (4 Sets), Section 3 VARC (2 RCs + 6 VA).
"""

import re
from pathlib import Path
from google import genai
import config

PLAN_OVERVIEW = """🎯 <b>CAT 2026 99+ Percentile Master Plan (Enhanced Format)</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ <b>Daily Routine:</b>
• <b>Section 0: Daily CAT Boosters</b>
  - 📐 Formula of the Day (with derivation & CAT example)
  - ⚡ Shortcut of the Day (time-saved metric)
  - 🧮 Speed Drill (5 mental math problems in 60s)
  - 📖 Vocabulary of the Day (5 CAT RC-level words with antonym & usage)
  - 🧠 Concept of the Day (Common traps & exam insights)

• <b>Section 1: Quantitative Aptitude (25–28 Qs)</b>
  - Block A: Number System | Block B: Arithmetic | Block C: Algebra
  - Block D: Geometry | Block E: Modern Math
  - Every Q includes: Priority (🟢/🟡/🔴), Recommended Time, Shortcut Hint, Watch Out Trap

• <b>Section 2: DILR (4 Complete Sets, 16 Qs)</b>
  - Arrangements, Tournaments, Distribution, Venn / Network Routes

• <b>Section 3: VARC (14 Qs)</b>
  - 2 Full RCs (Philosophy / Economics / Technology / Sociology)
  - 6 VA: 2 Para Summaries, 2 Para Jumbles, 1 Odd One Out, 1 Sentence Placement

• <b>Section 4: Complete Solutions</b>
  - Fastest CAT Method, Trap Analysis, and Concept Revision

━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 <b>Commands for Master Plan:</b>
• <code>/boosters</code> — Today's Formula, Shortcut, Speed Drill & Vocab
• <code>/shortcuts</code> — Full CAT 2026 Shortcut & Accuracy Bible
• <code>/syllabus</code> — Comprehensive Topic Weightage Reference
"""

PROMPT_TEMPLATE = """You are an elite CAT mentor creating the official CAT 2026 Daily Master Set for Day {day_num}.
Follow the CAT 2026 MASTER INSTRUCTIONS exactly:

Target: 99+ Percentile Track | 60-Day Sprint | Actual CAT Level.
Structure the response with exact markdown headers:

# ☀️ CAT 2026 Daily Set — Day {day_num}
### Target: 99+ Percentile

# SECTION 0 — DAILY CAT BOOSTERS
## 📐 0A. Formula of the Day (Rule, step-by-step, CAT problem solved)
## ⚡ 0B. Shortcut of the Day (Rule, conventional vs shortcut, time saved)
## 🧮 0C. Speed Drill — Solve All 5 in Under 60 Seconds
## 📖 0D. Vocabulary of the Day — 5 Words (Word, Meaning, Antonym, CAT RC Usage)
## 🧠 0E. Concept of the Day (Exam traps & nuances)

# SECTION 1 — QUANTITATIVE APTITUDE
25 to 28 questions categorized into:
- BLOCK A — NUMBER SYSTEM
- BLOCK B — ARITHMETIC
- BLOCK C — ALGEBRA
- BLOCK D — GEOMETRY
- BLOCK E — MODERN MATH
For EVERY question include: Source (CAT PYQ / CAT-Level Inspired), Topic, Type (MCQ/TITA), Difficulty (★-★★★★★), Expected Percentile, Recommended Time, Attempt Priority (🟢 Must Attempt / 🟡 Attempt Later / 🔴 Skip in Round 1), ⚡ Shortcut Hint, 🚨 Watch Out Trap.

# SECTION 2 — DATA INTERPRETATION & LOGICAL REASONING
4 Complete CAT-Level Sets with 4 questions each (16 questions total).

# SECTION 3 — VERBAL ABILITY & READING COMPREHENSION
- 2 Full RC Passages (4 questions each) on Philosophy, Economics, Sociology or Tech
- 6 VA Questions (2 Para Summaries, 2 Para Jumbles, 1 Odd One Out, 1 Sentence Placement)

# SECTION 4 — COMPLETE SOLUTIONS & STRATEGY ANALYSIS
Fastest CAT methods, shortcut tricks, and trap alerts for all questions.
"""

def get_master_plan() -> str:
    return PLAN_OVERVIEW

def generate_next_set(day_num: int) -> Path:
    """Generates a new master set using Gemini and saves it to Daily_Master_Sets."""
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    prompt = PROMPT_TEMPLATE.format(day_num=day_num)

    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=prompt
    )

    content = response.text.strip()
    target_file = config.DAILY_SETS_DIR / f"Day_{day_num}.md"
    target_file.write_text(content, encoding="utf-8")
    return target_file