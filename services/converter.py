import os
import sys
import urllib.request
from urllib.parse import urljoin
from utils import helper

def convert_markdown_to_pdf(markdown_file, output_file):
    # Convert markdown to html using github api
    github_api_url = 'https://api.github.com/markdown'
    headers = {'Content-Type': 'text/plain'}
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()
    req = urllib.request.Request(github_api_url, data=markdown_content.encode('utf-8'), headers=headers)
    try:
        response = urllib.request.urlopen(req)
        html_content = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f'Error converting markdown to html: {e}')
        sys.exit(1)

    # Save html content to a temporary file
    temp_html_file = 'temp.html'
    with open(temp_html_file, 'w') as f:
        f.write(html_content)

    # Convert html to pdf using wkhtmltopdf command
    wkhtmltopdf_command = f'wkhtmltopdf {temp_html_file} {output_file}'
    helper.run_command(wkhtmltopdf_command)

    # Remove temporary html file
    os.remove(temp_html_file)