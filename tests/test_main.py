import unittest
import os
import sys
from main import main

class TestMain(unittest.TestCase):
    def test_convert(self):
        # Create a test markdown file
        with open('test.md', 'w') as f:
            f.write('# Test Markdown File')

        # Convert the markdown file to pdf
        main(['-i', 'test.md', '-o', 'test.pdf'])

        # Check if the pdf file exists
        self.assertTrue(os.path.exists('test.pdf'))

        # Remove the test files
        os.remove('test.md')
        os.remove('test.pdf')

if __name__ == '__main__':
    unittest.main()