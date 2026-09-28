"""
parser.py
─────────
Parses Day_XX.md master sets (both standard and Enhanced CAT 2026 formats)
into structured sections for Telegram delivery.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional
import config

def get_day_file(day_num: int) -> Optional[Path]:
    candidates = [
        config.DAILY_SETS_DIR / f"Day_{day_num}.md",
        config.DAILY_SETS_DIR / f"Day_{day_num:02d}.md",
        config.CAT_PREP_DIR / f"CAT2026_Day{day_num:02d}_Enhanced.md",
        config.CAT_PREP_DIR / f"CAT2026_Day{day_num}_Enhanced.md",
        config.CAT_PREP_DIR / f"CAT2026_Day{day_num:02d}_MasterSet.md",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None

def list_available_days() -> List[int]:
    days = set()
    if config.DAILY_SETS_DIR.exists():
        for p in config.DAILY_SETS_DIR.glob("Day_*.md"):
            m = re.search(r"Day_(\d+)\.md", p.name)
            if m:
                days.add(int(m.group(1)))
    for p in config.CAT_PREP_DIR.glob("CAT2026_Day*.md"):
        m = re.search(r"Day(\d+)", p.name)
        if m:
            days.add(int(m.group(1)))
    return sorted(list(days))

def parse_day_set(day_num: int) -> Dict[str, str]:
    file_path = get_day_file(day_num)
    if not file_path:
        return {"error": f"Master Set for Day {day_num} not found."}

    text = file_path.read_text(encoding="utf-8")

    # Flexible matching for both formats (Section 0, 1, 2, 3, 4 OR Section I, II, III)
    s0_m = re.search(r"(#+\s*SECTION\s*(?:0\b|ZERO\b)[^\n]*)", text, re.IGNORECASE)
    s1_m = re.search(r"(#+\s*SECTION\s*(?:I\b|1\b)[^\n]*)", text, re.IGNORECASE)
    s2_m = re.search(r"(#+\s*SECTION\s*(?:II\b|2\b)[^\n]*)", text, re.IGNORECASE)
    s3_m = re.search(r"(#+\s*SECTION\s*(?:III\b|3\b)[^\n]*)", text, re.IGNORECASE)
    s4_m = re.search(r"(#+\s*(?:SECTION\s*(?:IV\b|4\b)|DETAILED SOLUTIONS|COMPLETE SOLUTIONS|STOP HERE)[^\n]*)", text, re.IGNORECASE)
    ans_m = re.search(r"(#+\s*FINAL ANSWER KEY[^\n]*)", text, re.IGNORECASE)
    notes_m = re.search(r"(#+\s*(?:CAT Mentor Analysis|CAT 99\+ TRAINING NOTES|SECTION 5)[^\n]*)", text, re.IGNORECASE)

    # Overview
    first_split = s0_m.start() if s0_m else (s1_m.start() if s1_m else 1000)
    overview = text[:first_split].strip()

    # Section 0: Boosters (Formula, Shortcut, Speed Drill, Vocab, Concept)
    boosters_text = ""
    if s0_m and s1_m:
        boosters_text = text[s0_m.start():s1_m.start()].strip()

    # Section 1: QA
    qa_text = ""
    if s1_m and s2_m:
        qa_text = text[s1_m.start():s2_m.start()].strip()

    # Section 2: DILR
    dilr_text = ""
    if s2_m and s3_m:
        dilr_text = text[s2_m.start():s3_m.start()].strip()

    # Section 3: VARC
    varc_end = s4_m.start() if s4_m else (ans_m.start() if ans_m else len(text))
    varc_text = ""
    if s3_m:
        varc_text = text[s3_m.start():varc_end].strip()

    # Solutions & Answers
    solutions_text = ""
    if s4_m:
        sol_end = ans_m.start() if ans_m else (notes_m.start() if notes_m else len(text))
        solutions_text = text[s4_m.start():sol_end].strip()

    answers_text = ""
    if ans_m:
        ans_end = notes_m.start() if notes_m else len(text)
        answers_text = text[ans_m.start():ans_end].strip()
    elif s4_m and not answers_text:
        # Answers may be inside Section 4
        answers_text = solutions_text[:1500]

    return {
        "day": day_num,
        "file_path": str(file_path),
        "overview": overview,
        "boosters": boosters_text,
        "qa": qa_text,
        "dilr": dilr_text,
        "varc": varc_text,
        "answers": answers_text,
        "solutions": solutions_text,
        "full_text": text
    }

def chunk_text(text: str, max_chars: int = 3800) -> List[str]:
    """Splits long markdown text safely by headers, dividers, or paragraphs."""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    paragraphs = re.split(r"(\n---+\n|\n###? |\n\n)", text)

    current_chunk = []
    current_len = 0

    for part in paragraphs:
        if not part:
            continue
        if current_len + len(part) > max_chars:
            if current_chunk:
                chunks.append("".join(current_chunk).strip())
                current_chunk = []
                current_len = 0
            if len(part) > max_chars:
                lines = part.split("\n")
                for line in lines:
                    if current_len + len(line) + 1 > max_chars:
                        chunks.append("".join(current_chunk).strip())
                        current_chunk = [line + "\n"]
                        current_len = len(line) + 1
                    else:
                        current_chunk.append(line + "\n")
                        current_len += len(line) + 1
            else:
                current_chunk.append(part)
                current_len += len(part)
        else:
            current_chunk.append(part)
            current_len += len(part)

    if current_chunk:
        chunks.append("".join(current_chunk).strip())

    return [c for c in chunks if c.strip()]