import subprocess
import os
from utils.helper import get_file_extension, get_file_name, get_file_directory

class MarkdownConverter:
    def convert(self, input_file, output_file):
        command = f'pandoc -s {input_file} -o {output_file}'
        subprocess.run(command, shell=True)