import os
import sys
from subprocess import run

def convert_markdown_to_pdf(input_file, output_file):
    # Use pandoc to convert Markdown to PDF
    pandoc_cmd = f'pandoc -s {input_file} -o {output_file}'
    try:
        run(pandoc_cmd, shell=True, check=True)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)