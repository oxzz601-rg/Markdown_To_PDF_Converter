import os
import sys

def get_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Error: File {file_path} does not exist.')
        sys.exit(1)

def write_to_file(file_path, contents):
    with open(file_path, 'w') as file:
        file.write(contents)
