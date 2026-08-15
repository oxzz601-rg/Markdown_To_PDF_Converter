import os
import subprocess
from utils.helper import get_markdown_content

def convert_markdown_to_pdf(input_file, output_file):
    markdown_content = get_markdown_content(input_file)
    # Use pandoc to convert Markdown to PDF
    try:
        subprocess.run(['pandoc', '-s', input_file, '-o', output_file], check=True)
    except FileNotFoundError:
        print('Error: Pandoc is not installed. Please install pandoc and try again.')
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f'Error: Failed to convert Markdown to PDF. {str(e)}')
        sys.exit(1)