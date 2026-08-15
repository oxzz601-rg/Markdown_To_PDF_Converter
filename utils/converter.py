import os
from markdown import markdown
from pdfkit import from_string
from ..helper import clean_markdown

def convert_markdown_to_pdf(markdown_file, output_file):
    with open(markdown_file, 'r') as f:
        markdown_text = f.read()
    clean_text = clean_markdown(markdown_text)
    html = markdown(clean_text)
    from_string(html, output_file)