import argparse
import os
from utils import markdown_to_pdf

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('--input', type=str, help='Input Markdown file')
    parser.add_argument('--output', type=str, help='Output PDF file', default='output.pdf')
    args = parser.parse_args()
    if not os.path.exists(args.input):
        print('Input file does not exist')
        exit(1)
    markdown_to_pdf(args.input, args.output)
    print(f'PDF saved to {args.output}')