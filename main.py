#!/usr/bin/env python3
import argparse
import subprocess
import os
from utils import helper

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF converter')
    parser.add_argument('-i', '--input', help='Input Markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file', required=True)
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    if not input_file.endswith('.md'):
        print('Error: Input file must be a Markdown file (.md)')
        return

    if not output_file.endswith('.pdf'):
        print('Error: Output file must be a PDF file (.pdf)')
        return

    helper.convert_markdown_to_pdf(input_file, output_file)

if __name__ == '__main__':
    main()