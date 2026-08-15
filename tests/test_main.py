import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):
    @patch('argparse.ArgumentParser')
    def test_main(self, mock_argparse):
        mock_argparse.return_value.parse_args.return_value.input_file = 'input.md'
        mock_argparse.return_value.parse_args.return_value.output = 'output.pdf'
        main()

if __name__ == '__main__':
    unittest.main()