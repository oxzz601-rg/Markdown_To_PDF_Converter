import os
import sys
import re
from argparse import ArgumentParser
from utils.converter import markdown_to_pdf

if __name__ == '__main__':
    parser = ArgumentParser(description='Markdown to PDF converter')
    parser.add_argument('-i', '--input', help='Input markdown file', required=True)
    parser.add_argument('-o', '--output', help='Output pdf file', required=True)
    args = parser.parse_args()
    markdown_to_pdf(args.input, args.output)