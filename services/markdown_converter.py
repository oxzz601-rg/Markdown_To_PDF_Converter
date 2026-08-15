import os
from utils import helper
from datetime import datetime

def convert(input_file, output_file):
    # Use pandoc to convert markdown to pdf
    command = f'pandoc -s {input_file} -o {output_file} --pdf-engine=xelatex'
    os.system(command)