#!/usr/bin/env python3
import argparse
import os
from utils import helper
from services import markdown_to_pdf

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('input_file', type=str, help='Markdown file to convert')
    parser.add_argument('-o', '--output', type=str, help='Output PDF file name')
    args = parser.parse_args()
    if not args.output:
        output_file = os.path.splitext(args.input_file)[0] + '.pdf'
    else:
        output_file = args.output
    markdown_to_pdf.convert(args.input_file, output_file)

if __name__ == '__main__':
    main()