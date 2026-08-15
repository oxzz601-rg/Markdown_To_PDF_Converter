#!/usr/bin/env python3
import subprocess
import os

def run_command(command):
    subprocess.run(command, shell=True)

def file_exists(file_path):
    return os.path.exists(file_path)
