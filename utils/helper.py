import os

def get_output_file(input_file):
    return os.path.splitext(input_file)[0] + '.pdf'