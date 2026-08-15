import os
from subprocess import run
from tempfile import TemporaryDirectory

def markdown_to_pdf(markdown_file, pdf_file):
    with TemporaryDirectory() as tmpdir:
        html_file = os.path.join(tmpdir, 'temp.html')
        pdf_file_tmp = os.path.join(tmpdir, 'temp.pdf')
        # Convert Markdown to HTML
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()
        with open(html_file, 'w') as f:
            f.write('<html><body>' + markdown_content.replace('#', '<h1>') + '</body></html>')
        # Convert HTML to PDF
        run(['wkhtmltopdf', html_file, pdf_file_tmp])
        # Copy PDF to output
        with open(pdf_file_tmp, 'rb') as f_in:
            with open(pdf_file, 'wb') as f_out:
                f_out.write(f_in.read())