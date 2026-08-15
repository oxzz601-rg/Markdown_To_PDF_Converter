import os
import subprocess

def run_command(command, cwd=None):
    try:
        subprocess.run(command, cwd=cwd, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        sys.exit(1)