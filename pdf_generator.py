from fpdf import FPDF
import os

class PDF(FPDF):
    def __init__(self, chapter_title):
        super().__init__()
        self.chapter_title = chapter_title

    def header(self):
        self.set_font("Ukij", size=12)
        self.cell(0, 10, self.chapter_title, ln=True, align="C")

    def chapter_body(self, text):
        self.set_font("Ukij", size=11)
        self.multi_cell(0, 10, text)

def generate_pdf(chapter_title, chapter_text, screenshot_path, chapter_num):
    pdf = PDF(f"Chapter {chapter_num}: {chapter_title}")

    # ✅ Add Unicode-capable font
    pdf.add_font("Ukij", "", "fonts/ukij-tuz-basma.ttf", uni=True)
    pdf.set_font("Ukij", size=12)

    pdf.add_page()
    pdf.ln(10)

    if screenshot_path and os.path.exists(screenshot_path):
        pdf.image(screenshot_path, w=pdf.w - 40)
        pdf.ln(10)

    pdf.chapter_body(chapter_text)

    os.makedirs("pdfs", exist_ok=True)
    output_path = f"pdfs/chapter_{chapter_num}.pdf"
    pdf.output(output_path)
