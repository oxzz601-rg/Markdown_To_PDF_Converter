import markdown
import pdfkit
import os

def convert_markdown_to_pdf(input_file, output_file):
    with open(input_file, 'r') as f:
        md = f.read()

    html = markdown.markdown(md)

    # Create a basic HTML template
    template = '<html><body>{}</body></html>'.format(html)

    # Save the HTML to a temporary file
    tmp_file = 'tmp.html'
    with open(tmp_file, 'w') as f:
        f.write(template)

    # Convert the HTML to PDF using pdfkit
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'quiet': '',
    }
    pdfkit.from_file(tmp_file, output_file, options=options)

    # Remove the temporary HTML file
    os.remove(tmp_file)