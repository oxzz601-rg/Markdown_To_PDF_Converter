#!/usr/bin/env python3
import subprocess
import os

def convert_markdown_to_pdf(input_file, output_file):
    # Use pandoc to convert Markdown to PDF
    pandoc_cmd = f'pandoc -s {input_file} -o {output_file}'
    subprocess.run(pandoc_cmd, shell=True)