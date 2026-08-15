import subprocess
import os

def convert_markdown_to_pdf(input_file, output_file):
    # Use pandoc to convert markdown to pdf
    command = f"pandoc -s {input_file} -o {output_file}"
    subprocess.run(command, shell=True)
