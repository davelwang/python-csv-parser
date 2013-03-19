#!/usr/bin/python

PROG_VERSION = "0.9"
PROG_USAGE = "Usage: %prog <options> inputfile"
PROG_DESC = """This program counts the number of entries in a CSV file and displays the result to stdout""" 

PROG_ARGNUM = 1

# import modules
import  sys
import  csv
import  optparse


def  count_entries(fname, inc_header):

    with  open(fname, 'rb') as f:
        reader = csv.reader(f)

        if  inc_header:
            reader.next()  # do not include header

        count = 0

        for  row in reader:
            count = count + 1


        outstr = "CSV file " + fname + " has " + str(count) + " entries, excluding header"

        print outstr

    
    return


def  main():
    parser = optparse.OptionParser(version = '%prog version ' + PROG_VERSION, \
        usage = PROG_USAGE, \
        description = PROG_DESC)
    parser.add_option('-i', '--header', help = 'input CSV file includes header', \
        dest = 'header', default = False, action = 'store_true')
    
    (opts, args) = parser.parse_args()

    if len(args) != PROG_ARGNUM:
        parser.error("incorrect number of arguments!")
    else:
        infile = args[0]

    count_entries(infile, opts.header)

    return

if  __name__ == "__main__":
    main()
