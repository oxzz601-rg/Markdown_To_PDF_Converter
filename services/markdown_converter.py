import os
import pdfkit
from markdown import markdown
from bs4 import BeautifulSoup

def convert(markdown_file, pdf_file):
    with open(markdown_file, 'r') as f:
        markdown_text = f.read()

    html = markdown(markdown_text)
    soup = BeautifulSoup(html, 'html.parser')

    # Remove unnecessary elements
    for element in soup.find_all(['script', 'style']):
        element.decompose()

    # Save HTML to temporary file
    temp_html_file = 'temp.html'
    with open(temp_html_file, 'w') as f:
        f.write(str(soup))

    # Convert HTML to PDF using pdfkit
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'no-outline': None,
        'quiet': ''
    }
    pdfkit.from_file(temp_html_file, pdf_file, options=options)

    # Remove temporary HTML file
    os.remove(temp_html_file)