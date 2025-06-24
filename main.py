# main.py
from scrape import fetch_content_and_screenshot
from ai_writer import spin_chapter
from ai_reviewer import review_chapter
from human_loop import human_edit
from versioning import save_version
from pdf_generator import generate_pdf
import os

base_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_{}"
output_folder = "chapters"
pdf_folder = "pdfs"

os.makedirs(output_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)

for chapter_num in range(1, 6):
    print(f"\n\U0001F4D8 Processing Chapter {chapter_num}...")

    url = base_url.format(chapter_num)
    raw_text, chapter_title, screenshot_path = fetch_content_and_screenshot(url, chapter_num)

    spun = spin_chapter(raw_text)
    reviewed = review_chapter(spun)
    final = human_edit(reviewed)

    chapter_filename = f"chapter_{chapter_num}.txt"
    with open(os.path.join(output_folder, chapter_filename), "w", encoding="utf-8") as f:
        f.write(final)


    generate_pdf(
        chapter_title,
        final,
        screenshot_path,
        chapter_num
    )

    save_version(final, chapter_num)
    print(f"\u2705 Chapter {chapter_num} saved.")
