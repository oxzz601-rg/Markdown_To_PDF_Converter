import os
import sys

def get_absolute_path(file_path):
    return os.path.abspath(file_path)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]
