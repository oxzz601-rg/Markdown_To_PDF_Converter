import os
import sys

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_directory(file_path):
    return os.path.dirname(file_path)