import argparse
import os
import sys
from utils import helper
from services import converter

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('input_file', help='Path to Markdown file')
    parser.add_argument('-o', '--output', help='Path to output PDF file')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} not found.')
        sys.exit(1)

    if not args.input_file.endswith('.md'):
        print(f'Error: Input file {args.input_file} is not a Markdown file.')
        sys.exit(1)

    if not args.output:
        output_file = os.path.splitext(args.input_file)[0] + '.pdf'
    else:
        output_file = args.output
        if not output_file.endswith('.pdf'):
            output_file += '.pdf'

    converter.convert_markdown_to_pdf(args.input_file, output_file)
    print(f'Success: Converted {args.input_file} to {output_file}')

if __name__ == '__main__':
    main()