#!/usr/bin/env python3
import os
from utils.helper import run_command, file_exists

class MarkdownToPdf:
    @staticmethod
    def convert(input_file, output_file):
        if not file_exists(input_file):
            print('Input file not found.')
            return
        command = f"pandoc -s {input_file} -o {output_file}"
        run_command(command)

if __name__ == '__main__':
    MarkdownToPdf().convert('input.md', 'output.pdf')
