"""
Problem:

Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.
"""
import unittest
from parameterized import parameterized_class
from pathlib import Path
import subprocess
import os


@parameterized_class(('input_file',), [
    ('artifact/data/popular-names.txt',),
    ('artifact/data/random-text.txt',)
])
class TestP11Chapter2(unittest.TestCase):

    def test_should_replace_tab_into_space(self):
        # Get the base name of the file (e.g., 'popular-names.txt')
        base_name_input_file = os.path.basename(self.input_file)
        # Split the base name into name and extension (e.g., 'popular-names'
        # and '.txt')
        file_name_input, file_extension = os.path.splitext(
            base_name_input_file)

        expected_output_file = f"artifact/data/{file_name_input}-expected-p11.txt"
        # Check if expected file output exists or not
        if not Path(expected_output_file).is_file():
            # If does not exist, then create the expected output
            with open(self.input_file, 'r') as infile, open(expected_output_file, 'w') as outfile:
                for line in infile:
                    # Replace all tab characters with a space in the current
                    # line
                    modified_line = line.replace('\t', ' ')
                    # Write the modified line to the output file
                    outfile.write(modified_line)

        actual_output_file = f"artifact/data/{file_name_input}-actual-p11.txt"
        # Call the solution script with two arguments
        result = subprocess.run(
            ['./src/p11.sh', self.input_file, actual_output_file], text=True)

        self.assertTrue(
            check_if_two_files_are_same(
                actual_output_file,
                expected_output_file))


def check_if_two_files_are_same(
        actual_output_file: str, expected_output_file: str) -> bool:
    with open(actual_output_file, 'r') as actual_output, open(expected_output_file, 'r') as expected_output:
        line_num = 1
        while True:
            line_actual = actual_output.readline()
            line_expected = expected_output.readline()
            # If both lines are empty, end of both files is reached
            if not line_actual and not line_expected:
                print("Files are identical.")
                return True

            # If one file ends before the other
            if not line_actual or not line_expected:
                print(f"Files differ at line {line_num}.")
                return False

            # If lines are different
            if line_actual != line_expected:
                print(f"Files differ at line {line_num}.")
                return False

            line_num += 1


if __name__ == "__main__":
    unittest.main()
