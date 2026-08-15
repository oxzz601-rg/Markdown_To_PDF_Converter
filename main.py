import argparse
import os
import markdown
from xhtml2pdf import pisa
from bs4 import BeautifulSoup

def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

def convert_html_to_pdf(html, output_filename):
    with open(output_filename, 'wb') as f:
        pisa.CreatePDF(html, dest=f)

def main():
    parser = argparse.ArgumentParser(description='Markdown to PDF converter')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PDF file')
    args = parser.parse_args()

    if not args.output:
        output_filename = os.path.splitext(args.input_file)[0] + '.pdf'
    else:
        output_filename = args.output

    with open(args.input_file, 'r') as f:
        markdown_text = f.read()

    html = convert_markdown_to_html(markdown_text)
    soup = BeautifulSoup(html, 'html.parser')
    styled_html = str(soup)

    convert_html_to_pdf(styled_html, output_filename)

    print(f'PDF saved to {output_filename}')

if __name__ == '__main__':
    main()
