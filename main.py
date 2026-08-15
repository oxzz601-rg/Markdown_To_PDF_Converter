import argparse
import os
import sys
from utils.helper import convert_markdown_to_pdf

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('-i', '--input', required=True, help='Input Markdown file')
    parser.add_argument('-o', '--output', required=True, help='Output PDF file')
    args = parser.parse_args()
    convert_markdown_to_pdf(args.input, args.output)
