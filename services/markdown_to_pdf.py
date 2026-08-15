import os
import sys
from markdown import markdown
from pdfkit import from_string
from utils.helper import get_file_extension, get_file_name

class MarkdownToPdfConverter:
    def convert(self, input_file, output_file):
        try:
            with open(input_file, 'r') as f:
                markdown_text = f.read()
            html = markdown(markdown_text)
            from_string(html, output_file)
        except Exception as e:
            print(f'Error converting {input_file}: {str(e)}')
            sys.exit(1)

markdown_to_pdf = MarkdownToPdfConverter()