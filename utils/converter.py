import os
import markdown
import pdfkit
from ..helper import get_file_extension

def convert_markdown_to_pdf(input_file, output_file):
    # Check if input file is a Markdown file
    if get_file_extension(input_file) != '.md':
        raise ValueError('Input file must be a Markdown file')

    # Check if output file is a PDF file
    if get_file_extension(output_file) != '.pdf':
        raise ValueError('Output file must be a PDF file')

    # Read the Markdown file
    with open(input_file, 'r') as file:
        markdown_text = file.read()

    # Convert Markdown to HTML
    html = markdown.markdown(markdown_text)

    # Convert HTML to PDF
    pdfkit.from_string(html, output_file)
