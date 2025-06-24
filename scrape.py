# scrape.py
import requests
from bs4 import BeautifulSoup
from screenshotter import take_screenshot

def fetch_content_and_screenshot(url, chapter_num):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    content_div = soup.find("div", {"class": "mw-parser-output"})
    paragraphs = content_div.find_all("p")
    raw_text = "\n".join(p.text for p in paragraphs if p.text.strip())

    chapter_title = soup.title.string.strip()
    screenshot_path = take_screenshot(url, chapter_num)
    
    return raw_text, chapter_title, screenshot_path
