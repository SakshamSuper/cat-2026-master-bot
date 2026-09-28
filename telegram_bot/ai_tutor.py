"""
ai_tutor.py
───────────
Gemini AI CAT 2026 99+ Percentile Mentor for instant doubts, explanations, and topic drills.
"""

from google import genai
import config
from parser import parse_day_set

SYSTEM_PROMPT = """You are an expert CAT mentor trained to guide serious aspirants toward the 99+ percentile in CAT 2026.
You are familiar with the 65-day CAT Master Set repository (34 questions/day: QA, DILR, VARC).
When answering questions or doubts:
1. Provide intuitive, conceptual explanations first, then show the mathematical derivation.
2. Always highlight the time-saving shortcut or trick and note the common trap that candidates fall into.
3. Keep formatting clean and readable for mobile Telegram display (use bullet points, bold key terms).
4. Maintain a supportive, disciplined, and high-performance mindset.
"""

def get_gemini_client():
    return genai.Client(api_key=config.GEMINI_API_KEY)

def answer_doubt(query: str, current_day: int = None) -> str:
    """Answers candidate doubts using Gemini AI, with optional day context."""
    client = get_gemini_client()
    context = ""
    if current_day:
        data = parse_day_set(current_day)
        if "error" not in data:
            # Provide snippet of QA / DILR / VARC
            context = f"\n[Context for Day {current_day}]:\nOverview: {data['overview'][:500]}\n"
    
    prompt = f"{SYSTEM_PROMPT}\n{context}\nStudent Query: {query}\n\nProvide a clear, high-yield explanation with shortcuts and trap alerts:"
    try:
        resp = client.models.generate_content(
            model=config.GEMINI_MODEL,
            contents=prompt
        )
        return resp.text.strip()
    except Exception as e:
        return f"⚠️ Mentor AI temporary issue: {e}"

def generate_topic_drill(topic: str) -> str:
    """Generates a quick 3-question CAT drill on any requested topic."""
    client = get_gemini_client()
    prompt = (
        f"{SYSTEM_PROMPT}\n"
        f"Generate a quick 3-Question CAT drill on '{topic}' at actual CAT difficulty (Level 3-4).\n"
        f"Format:\n"
        f"1. 3 questions (MCQ/TITA with options and recommended time).\n"
        f"2. Answer Key.\n"
        f"3. Short step-by-step solution, shortcut trick, and trap alert for each."
    )
    try:
        resp = client.models.generate_content(
            model=config.GEMINI_MODEL,
            contents=prompt
        )
        return resp.text.strip()
    except Exception as e:
        return f"⚠️ Could not generate drill: {e}"
