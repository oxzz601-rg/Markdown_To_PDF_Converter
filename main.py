import argparse
import os
from utils.converter import convert_markdown_to_pdf

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('-i', '--input', help='Input Markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file', required=True)
    args = parser.parse_args()

    convert_markdown_to_pdf(args.input, args.output)
