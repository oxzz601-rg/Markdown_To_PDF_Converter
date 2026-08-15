import argparse
import os
import sys
from utils import helper
from services import markdown_converter

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('--input', type=str, help='Input Markdown file', required=True)
    parser.add_argument('--output', type=str, help='Output PDF file', required=True)
    args = parser.parse_args()

    markdown_file = args.input
    pdf_file = args.output

    if not os.path.exists(markdown_file):
        print(f'Error: {markdown_file} does not exist.')
        sys.exit(1)

    markdown_converter.convert(markdown_file, pdf_file)

if __name__ == '__main__':
    main()