import os
import sys
from subprocess import Popen, PIPE
from urllib.request import urlretrieve
from helper import get_absolute_path, get_file_extension

class MarkdownToPdfConverter:
    def __init__(self):
        self.pandoc_url = 'https://github.com/jgm/pandoc/releases/download/2.19/pandoc-2.19-windows.zip'
        self.pandoc_path = get_absolute_path('pandoc.exe')

    def download_pandoc(self):
        if not os.path.exists('pandoc.exe'):
            print('Downloading pandoc...')
            urlretrieve(self.pandoc_url, 'pandoc.zip')
            import zipfile
            with zipfile.ZipFile('pandoc.zip', 'r') as zip_ref:
                zip_ref.extractall()
            os.remove('pandoc.zip')

    def convert(self, input_file, output_file):
        self.download_pandoc()
        pandoc_command = f'{self.pandoc_path} -s {input_file} -o {output_file} --pdf-engine=wkhtmltopdf'
        process = Popen(pandoc_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode != 0:
            print(f'Error converting {input_file} to {output_file}: {error.decode()}')
            sys.exit(1)
        else:
            print(f'Successfully converted {input_file} to {output_file}')

def convert(input_file, output_file):
    converter = MarkdownToPdfConverter()
    converter.convert(input_file, output_file)
