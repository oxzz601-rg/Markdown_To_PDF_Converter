import unittest
from utils.helper import convert_markdown_to_pdf

class TestHelper(unittest.TestCase):
    def test_convert_markdown_to_pdf(self):
        # Create a temporary markdown file
        with open('test.md', 'w') as f:
            f.write('# Test\nThis is a test.\n')
        # Convert the markdown file to pdf
        convert_markdown_to_pdf('test.md', 'test.pdf')
        # Check if the pdf file is created
        self.assertTrue(os.path.exists('test.pdf'))
        # Remove the temporary files
        os.remove('test.md')
        os.remove('test.pdf')

if __name__ == '__main__':
    unittest.main()