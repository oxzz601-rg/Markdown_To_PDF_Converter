import argparse
import os
import sys
from utils.helper import convert_markdown_to_pdf

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Markdown to PDF converter')
    parser.add_argument('input_file', help='Path to the Markdown file')
    parser.add_argument('-o', '--output', help='Path to the output PDF file')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} does not exist')
        sys.exit(1)

    output_file = args.output if args.output else os.path.splitext(args.input_file)[0] + '.pdf'
    convert_markdown_to_pdf(args.input_file, output_file)
    print(f'Successfully converted {args.input_file} to {output_file}')