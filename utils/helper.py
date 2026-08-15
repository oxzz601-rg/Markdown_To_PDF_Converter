import os
import sys

def get_markdown_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Error: File {file_path} not found.')
        sys.exit(1)

def save_pdf_content(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f'Error: Failed to save PDF content. {str(e)}')
        sys.exit(1)