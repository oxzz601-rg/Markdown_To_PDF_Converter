import argparse
import os
import sys
from utils import helper
from utils import markdown_to_pdf

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF converter')
    parser.add_argument('-i', '--input', help='Input Markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file')
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output if args.output else input_file.replace('.md', '.pdf')

    if not os.path.exists(input_file):
        print(f'Input file {input_file} does not exist')
        sys.exit(1)

    markdown_to_pdf.convert(input_file, output_file)

if __name__ == '__main__':
    main()