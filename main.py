import argparse
import os
from utils.converter import convert_markdown_to_pdf

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('-i', '--input', help='Input Markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file', required=True)
    args = parser.parse_args()
    convert_markdown_to_pdf(args.input, args.output)

if __name__ == '__main__':
    main()