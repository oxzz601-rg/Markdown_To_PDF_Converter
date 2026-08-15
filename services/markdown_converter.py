# Service module for Markdown to PDF conversion
import os
import pdfkit
import markdown

# Function to convert Markdown to PDF
def convert(input_file, output_file):
    # Read Markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Convert HTML to PDF
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'header-spacing': '5',
    }
    pdfkit.from_string(html_content, output_file, options=options)