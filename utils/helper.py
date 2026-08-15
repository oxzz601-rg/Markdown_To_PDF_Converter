import os
import sys

def is_file_exists(file_path):
    return os.path.exists(file_path)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]