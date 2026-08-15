import os
import sys
import argparse
from utils import converter
from utils import helper

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF converter')
    parser.add_argument('input_file', type=str, help='Markdown file to convert')
    parser.add_argument('-o', '--output', type=str, help='Output PDF file')
    args = parser.parse_args()

    if not args.output:
        output_file = os.path.splitext(args.input_file)[0] + '.pdf'
    else:
        output_file = args.output

    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} not found')
        sys.exit(1)

    converter.convert_markdown_to_pdf(args.input_file, output_file)
    print(f'Conversion complete: {output_file}')

if __name__ == '__main__':
    main()