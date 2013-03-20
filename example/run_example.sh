#!/usr/bin/bash

# live example to illustrate the usage of python CSV processing scripts
#
# Input files:
# 1.  example_csv1.csv - CSV with 15 columns and 6 rows, with 1 row of header
# 2.  example_csv2.csv - CSV with 15 columns and 5 rows, with 1 row of header
# 3.  example_csv3.csv - CSV with 15 columns and 6 rows, with no header
# 4.  hdrs.desired - text file with the name of each wanted columns as rows, with header names
# 5.  hdrs.desired.noname - text file with each desired column number as rows
#
# In this example, the objective is to combine the CSV files, but with only columns 1-4, 7, and 12-14 in the end


# first, clean up
rm -f *.out


# get the headers and store them in a file
../get_csv_hdr.py -V example_csv1.csv > hdrs.out
echo "Content of hdrs.out:"
cat  hdrs.out
echo
echo

# in real life, one would manually edit hdrs.out to indicated which columns to keep
# here we use the pre-populated file "hdrs.desired" as if we manually changed hdrs.out

# here we prune the headers for the first file, example_csv1.csv
# note that the options indicate:
#   1. the input CSV file has headers (-t)
#   2. write the headers to output file as well (-o)
../prune_csv_col.py -t -o example_csv1.csv hdrs.desired example_combined.out

# then we process the second example file, example_csv2.csv
# note that the options indicate:
#   1. the input CSV file has headers (-t)
#   2. do not write the headers to the output file, because we are appending the rows in an existing file (example_combined.out)
../prune_csv_col.py -t example_csv2.csv hdrs.desired example_combined.out

# finally we process the third example file, example_csv3.csv
# note that the options indicate:
#  1. the input CSV file does not have headers
#  2. do not write the headers to the output file
../prune_csv_col.py example_csv3.csv hdrs.desired.noname example_combined.out

echo "content of example_combined.out"
cat example_combined.out
echo
echo
