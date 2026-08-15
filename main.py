# Import required libraries
import os
import sys
import argparse
from utils import helper
from services import markdown_converter

# Define main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('input_file', type=str, help='Markdown file to convert')
    parser.add_argument('-o', '--output', type=str, help='Output PDF file name', default='output.pdf')
    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} does not exist.')
        sys.exit(1)

    # Convert Markdown to PDF
    markdown_converter.convert(args.input_file, args.output)

    print(f'Markdown file {args.input_file} converted to {args.output} successfully.')

# Run main function
if __name__ == '__main__':
    main()