import argparse
import os
import sys
from utils import helper
from services import markdown_to_pdf

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PDF file')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} does not exist.')
        sys.exit(1)

    output_file = args.output if args.output else os.path.splitext(args.input_file)[0] + '.pdf'
    markdown_to_pdf.convert(args.input_file, output_file)
    print(f'Markdown file {args.input_file} converted to PDF {output_file}')

if __name__ == '__main__':
    main()