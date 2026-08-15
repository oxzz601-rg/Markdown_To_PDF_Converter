import os
import sys
from markdown import markdown
from pdfkit import from_string
from argparse import ArgumentParser

def convert_markdown_to_pdf(markdown_file, pdf_file):
    with open(markdown_file, 'r') as file:
        markdown_text = file.read()
    html = markdown(markdown_text)
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'quiet': '',
    }
    from_string(html, pdf_file, options=options)

def main():
    parser = ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('markdown_file', help='Path to Markdown file')
    parser.add_argument('-o', '--output', help='Path to output PDF file')
    args = parser.parse_args()
    if args.output:
        pdf_file = args.output
    else:
        base, ext = os.path.splitext(args.markdown_file)
        pdf_file = base + '.pdf'
    convert_markdown_to_pdf(args.markdown_file, pdf_file)
    print(f'Converted {args.markdown_file} to {pdf_file}')

if __name__ == '__main__':
    main()
