import os
import sys
from datetime import datetime

def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def print_progress(message):
    print(f'{get_current_time()} - {message}')