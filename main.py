import os
import sys
import argparse
from utils import markdown_helper
from services import pdf_service

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('-i', '--input', help='Input Markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file', required=True)
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    markdown_helper.convert_markdown(input_file)
    pdf_service.generate_pdf(input_file.replace('.md', '.html'), output_file)

if __name__ == '__main__':
    main()