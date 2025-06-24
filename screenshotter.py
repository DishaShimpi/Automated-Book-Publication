# screenshotter.py
import os
from playwright.sync_api import sync_playwright

def take_screenshot(url, chapter_num):
    chapter_folder = f"screenshots/chapter_{str(chapter_num).zfill(2)}"
    os.makedirs(chapter_folder, exist_ok=True)

    screenshot_path = os.path.join(chapter_folder, "screenshot.png")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=screenshot_path, full_page=True)
        browser.close()

    return screenshot_path
