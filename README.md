python-csv-parser
=================

Python implementation of a CSV parser, to prune unwanted columns in large CSV files.  Also includes other useful CSV utilities

The idea is that a script (get_csv_header.py) would grab the headers off a CSV file and store the result as a file, which would then allow the user to select which headers to keep.

After the user had edited the stored header file to include only the desired headers, the second script (prune_csv_col.py) could be used to prune the unwanted columns.
