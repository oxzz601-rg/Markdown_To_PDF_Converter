import os
import sys
from markdown import markdown
from pdfkit import from_string
from ..helper import validate_file_path

def markdown_to_pdf(input_file, output_file):
    validate_file_path(input_file)
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html_content = markdown(markdown_content)
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'no-outline': None
    }
    from_string(html_content, output_file, options=options)