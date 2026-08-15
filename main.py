import argparse
import os
from utils.converter import convert_markdown_to_pdf

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PDF file')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print('Input file does not exist')
        return

    output_file = args.output if args.output else args.input_file.replace('.md', '.pdf')
    convert_markdown_to_pdf(args.input_file, output_file)
    print(f'PDF saved to {output_file}')

if __name__ == '__main__':
    main()