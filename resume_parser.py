import pdfplumber
import docx2txt

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)
