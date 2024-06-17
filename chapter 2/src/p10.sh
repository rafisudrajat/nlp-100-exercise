#!/bin/sh
<<'###BLOCK-COMMENT'
Problem:

Count the number of lines of the file. Confirm the result by using wc command.
###BLOCK-COMMENT

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "No file provided"
    exit 1
fi

output=$(wc -l < "$1")
# Extract the number of lines using awk
num_lines=$(echo $output | awk '{print $1}')

echo $num_lines