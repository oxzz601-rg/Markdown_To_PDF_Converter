import argparse
import subprocess
import os
from utils.helper import convert_markdown_to_pdf

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('--input', help='Markdown file to convert', required=True)
    parser.add_argument('--output', help='Output PDF file', required=True)
    args = parser.parse_args()
    convert_markdown_to_pdf(args.input, args.output)
