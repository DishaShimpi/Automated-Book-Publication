# 📚 Automated-Book-Publication

This project implements an **AI-driven automated book publication system**. It scrapes online book chapters, rewrites and refines content using LLMs, includes human-in-the-loop editing, and exports each chapter with screenshots to a structured PDF—all **without calling any external APIs**.

---

## 🚀 Features

✅ Scrape content from Wikisource chapters  
✅ Take screenshots of each chapter using **Playwright**  
✅ Auto-generate rewritten content using an **LLM**  
✅ AI-Reviewed and human-editable CLI interface  
✅ Store chapter versions in **ChromaDB** with unique IDs  
✅ Export each chapter to a polished **PDF with images**  
✅ Fully local (NO API calls or paid keys needed)  

---

## 📂 Sample Source

Currently configured to process:  
📘 [The Gates of Morning - Book 1 - Chapter 1](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1)

You can modify the `base_url` in `main.py` to iterate through multiple chapters.

---

## 🛠️ Requirements
Install all dependencies using:
```bash
pip install -r requirements.txt
```
Additionally, install Playwright browser support:
```bash
playwright install
```

## 🔤 Font Setup
I have used a Unicode-compatible TTF font to render clean multilingual text in PDFs.

  1. Download the font ukij-tuz Basma or any .ttf font that supports extended characters
    📥 Example font download
  2. Place the font inside a fonts/ directory:
```bash
autobook/
├── fonts/
│   └── ukij.ttf
```


## ▶️ How to Run
```bash
python main.py
```

Each chapter will:

  Be scraped and saved as a screenshot
  
  Be rewritten by the AI
  
  Ask you for human edits (yes/no)
  
  Be saved into ChromaDB
  
  Exported to:
```bash
chapter_X.txt
pdfs/chapter_X.pdf
screenshots/chapter_X/chapter.png
```
You’ll also get the final Chapter ID from ChromaDB.

## 💾 Chapter Retrieval (Optional)
You can retrieve previously saved chapters by running:
```bash
python view_chapter.py
```
Paste the Chapter ID when prompted to view the versioned content.
