import argparse
import json
import os
import sys
from utils import helper
from services import markdown_converter

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF Converter')
    parser.add_argument('-i', '--input', help='Input Markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output PDF file', required=True)
    args = parser.parse_args()
    converter = markdown_converter.MarkdownConverter()
    converter.convert(args.input, args.output)

if __name__ == '__main__':
    main()