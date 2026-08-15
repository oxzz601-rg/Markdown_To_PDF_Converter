import os
import sys
from subprocess import Popen, PIPE

def generate_pdf(input_file, output_file):
    command = ['wkhtmltopdf', input_file, output_file]
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print('Error generating PDF:', stderr.decode('utf-8'))