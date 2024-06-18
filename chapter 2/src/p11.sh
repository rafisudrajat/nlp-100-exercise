#!/bin/sh
<<'###BLOCK-COMMENT'
Problem:

Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.
###BLOCK-COMMENT

# Check if the number of arguments is exactly 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_file> <output_file>"
    exit 1
fi

input_file=$1
output_file=$2

tr '\t' ' ' < $input_file > $output_file
