import os
from utils.helper import get_file_extension

def convert_markdown_to_pdf(markdown_file, pdf_file):
    if get_file_extension(markdown_file) != '.md':
        raise ValueError('Input file must be a Markdown file')
    if get_file_extension(pdf_file) != '.pdf':
        raise ValueError('Output file must be a PDF file')
    # Convert Markdown to PDF using subprocess and pandoc
    # For this example, we assume pandoc is installed and available in the system's PATH
    pandoc_command = f"pandoc -s {markdown_file} -o {pdf_file}"
    os.system(pandoc_command)