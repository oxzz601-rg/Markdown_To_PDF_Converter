import os
import sys
from utils import helper
from datetime import datetime
import subprocess

class MarkdownToPdf:
    @staticmethod
    def convert(markdown_file, pdf_file):
        # Use pandoc to convert markdown to pdf
        pandoc_cmd = f'pandoc -s {markdown_file} -o {pdf_file}'
        subprocess.run(pandoc_cmd, shell=True)

        print(f'Markdown file {markdown_file} converted to PDF: {pdf_file}')