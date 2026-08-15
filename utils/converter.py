import os
from markdown import markdown
from utils.helper import run_command
import pdfkit

def convert_markdown_to_pdf(input_file, output_file):
    with open(input_file, 'r') as f:
        md_content = f.read()
    html_content = markdown(md_content)
    with open('temp.html', 'w') as f:
        f.write(html_content)
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'quiet': '',
    }
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_file('temp.html', output_file, options=options, configuration=config)
    os.remove('temp.html')