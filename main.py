import argparse
import os
import sys
from utils import helper
from services import pdf_converter

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('-i', '--input', required=True, help='Input Markdown file')
    parser.add_argument('-o', '--output', required=True, help='Output PDF file')
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    if not os.path.exists(input_file):
        print(f'Error: Input file {input_file} does not exist.')
        sys.exit(1)
    pdf_converter.convert(input_file, output_file)

if __name__ == '__main__':
    main()