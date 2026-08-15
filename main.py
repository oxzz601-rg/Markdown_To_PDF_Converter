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

    input_file = args.input
    output_file = args.output

    if not os.path.exists(input_file):
        print(f'Error: Input file {input_file} does not exist.')
        sys.exit(1)

    markdown_converter.convert(input_file, output_file)

if __name__ == '__main__':
    main()