import os
import sys
import argparse
from utils import helper
from services import markdown_to_pdf

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('-i', '--input', help='Input markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file', required=True)
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f'Input file {args.input} does not exist.')
        return

    markdown_to_pdf.convert(args.input, args.output)

if __name__ == '__main__':
    main()