import os
import re

def clean_markdown(markdown_text):
    # Remove any HTML tags
    markdown_text = re.sub(r'<.*?>', '', markdown_text)
    return markdown_text

def get_pdf_filename(markdown_filename):
    return markdown_filename.replace('.md', '.pdf')