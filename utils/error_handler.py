import sys

class ErrorHandler:
    @staticmethod
    def handle_error(message):
        print(f'Error: {message}')
        sys.exit(1)
