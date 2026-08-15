import os
import sys
from subprocess import Popen, PIPE

def convert_markdown_to_pdf(input_file, output_file):
    try:
        # Use pandoc to convert Markdown to PDF
        pandoc_cmd = ['pandoc', '-f', 'markdown', '-t', 'latex', '-o', output_file, input_file]
        process = Popen(pandoc_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f'Error: {stderr.decode()}', file=sys.stderr)
            sys.exit(1)
        print(f'Conversion successful: {input_file} -> {output_file}')
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
