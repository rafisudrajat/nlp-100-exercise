"""
Problem:

Count the number of lines of the file. Confirm the result by using wc command.
"""

import unittest
from parameterized import parameterized_class

import subprocess


@parameterized_class(('text_file_path', 'line_numbers'), [
    ('artifact/data/popular-names.txt', 2780),
    ('artifact/data/random-text.txt', 17)
])
class TestP10Chapter2(unittest.TestCase):
    def test_should_count_lines(self):
        # Run the bash script and capture the output
        result = subprocess.run(
            ['./src/p10.sh', self.text_file_path], capture_output=True, text=True)
        # Check if the script ran successfully
        if result.returncode == 0:
            # Get the output and split to get the number of lines
            output = result.stdout.strip()
            self.assertEqual(int(output), self.line_numbers)
        else:
            print(f"Error: {result.stderr}")


if __name__ == "__main__":
    unittest.main()
