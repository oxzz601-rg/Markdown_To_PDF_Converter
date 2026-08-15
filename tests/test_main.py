import unittest
import os
import sys
import tempfile
import shutil
from main import main
from utils.helper import convert_markdown_to_pdf

class TestMarkdownToPDFConverter(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.input_file = os.path.join(self.temp_dir, 'input.md')
        self.output_file = os.path.join(self.temp_dir, 'output.pdf')
        with open(self.input_file, 'w') as f:
            f.write('# Test
This is a test.')

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_convert_markdown_to_pdf(self):
        convert_markdown_to_pdf(self.input_file, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

if __name__ == '__main__':
    unittest.main()
