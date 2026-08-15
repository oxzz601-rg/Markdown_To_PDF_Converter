import os
from utils import helper
from subprocess import Popen, PIPE

class MarkdownToPdf:
    @staticmethod
    def convert(input_file, output_file):
        helper.print_progress('Converting Markdown to PDF...')
        try:
            command = f'pandoc -s {input_file} -o {output_file}'
            process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            output, error = process.communicate()
            if process.returncode != 0:
                raise Exception(error.decode('utf-8'))
            helper.print_progress('Conversion successful')
        except Exception as e:
            helper.print_progress(f'Conversion failed: {str(e)}')

markdown_to_pdf = MarkdownToPdf()