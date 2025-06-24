# auto_book_pub/agentic_pipeline.py
from ai_writer import spin_chapter
from ai_reviewer import review_chapter

def process_content(content):
    spun = spin_chapter(content)
    reviewed = review_chapter(spun)
    return reviewed