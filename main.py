import argparse
import os
import sys
from utils import helper
from services import markdown_converter

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('-i', '--input', help='Input Markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file', required=True)
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print('Input file not found.')
        sys.exit(1)

    markdown_converter.convert_markdown_to_pdf(args.input, args.output)

if __name__ == '__main__':
    main()