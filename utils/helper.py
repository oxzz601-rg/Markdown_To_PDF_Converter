import os
import re

def validate_file_path(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File {file_path} does not exist')
    if not os.path.isfile(file_path):
        raise IsADirectoryError(f'{file_path} is not a file')