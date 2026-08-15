import os
import sys
from utils.helper import is_file_exists, get_file_extension
from subprocess import call

def convert_markdown_to_pdf(markdown_file, pdf_file):
    if not is_file_exists(markdown_file):
        print('Input file not found.')
        sys.exit(1)

    if get_file_extension(markdown_file) != '.md':
        print('Input file is not a Markdown file.')
        sys.exit(1)

    if get_file_extension(pdf_file) != '.pdf':
        print('Output file is not a PDF file.')
        sys.exit(1)

    call(['pandoc', '-s', '--pdf-engine=wkhtmltopdf', markdown_file, '-o', pdf_file])