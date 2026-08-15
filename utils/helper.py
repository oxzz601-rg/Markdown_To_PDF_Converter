import os
import sys
import re
from html import escape

def convert_markdown(markdown_file):
    with open(markdown_file, 'r') as file:
        markdown_content = file.read()
    html_content = ''
    lines = markdown_content.split('\n')
    for line in lines:
        if line.startswith('# '):
            html_content += '<h1>' + line[2:] + '</h1>'
        elif line.startswith('## '):
            html_content += '<h2>' + line[3:] + '</h2>'
        elif line.startswith('### '):
            html_content += '<h3>' + line[4:] + '</h3>'
        elif line.startswith('- '):
            html_content += '<li>' + line[2:] + '</li>'
        else:
            html_content += '<p>' + escape(line) + '</p>'
    output_file = markdown_file.replace('.md', '.html')
    with open(output_file, 'w') as file:
        file.write('<html><body>' + html_content + '</body></html>')