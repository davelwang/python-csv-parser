#!/usr/bin/python

PROG_VERSION = "0.9"
PROG_USAGE = "Usage: %prog <options> inputfile"
PROG_DESC = """This program reads and displays the headers in a CSV file, assuming that the
first line of the CSV is the header.

It prints the headers to screen"""
PROG_ARGNUM = 1

# import modules
import  sys
import  csv
import  optparse


def  get_csv_header(fname, verbose):

    with  open(fname, 'rb') as f:
        reader = csv.reader(f)

        header = reader.next()

        for  i in xrange(0,len(header)):
            if  verbose:
                print "%d:%s" % (i + 1, header[i])
            else:
                print header[i]
    
    return


def  main():
    parser = optparse.OptionParser(version = '%prog version ' + PROG_VERSION, \
        usage = PROG_USAGE, \
        description = PROG_DESC)
    parser.add_option('-V', '--verbose', help = 'verbose mode, display the line number before header', \
        dest = 'verbose', default = False, action = 'store_true')
    
    (opts, args) = parser.parse_args()

    if len(args) != PROG_ARGNUM:
        parser.error("incorrect number of arguments!")
    else:
        infile = args[0]

    get_csv_header(infile, opts.verbose)

    return

if  __name__ == "__main__":
    main()
