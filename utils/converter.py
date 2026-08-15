import os
import sys
from subprocess import run

def convert_markdown_to_pdf(input_file, output_file):
    # Use pandoc to convert markdown to pdf
    command = ['pandoc', '-s', input_file, '-o', output_file]
    run(command, check=True)