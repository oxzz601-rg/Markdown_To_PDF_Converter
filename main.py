import os
import sys
import argparse
from utils import helper
from services import converter

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PDF file')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print('Input file does not exist.')
        sys.exit(1)

    output_file = args.output if args.output else os.path.splitext(args.input_file)[0] + '.pdf'
    converter.convert_markdown_to_pdf(args.input_file, output_file)

if __name__ == '__main__':
    main()