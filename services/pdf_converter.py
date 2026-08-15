import os
import sys
from utils.helper import get_file_contents
from utils.helper import write_to_file
import subprocess

def convert(markdown_file, pdf_file):
    # Convert Markdown to PDF using pandoc
    try:
        subprocess.run(['pandoc', '-s', markdown_file, '-o', pdf_file])
    except FileNotFoundError:
        print('Error: pandoc is not installed.')
        sys.exit(1)
