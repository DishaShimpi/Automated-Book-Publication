# auto_book_pub/ai_reviewer.py
from ai_writer import spin_chapter as call_llm

def review_chapter(content):
    prompt = f"Improve the grammar, clarity, and flow of the following text:\n\n{content}"
    return call_llm(prompt)
