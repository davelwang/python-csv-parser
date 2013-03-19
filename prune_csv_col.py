#!/usr/bin/python

PROG_VERSION = "0.9"
PROG_USAGE = "Usage: %prog <options> input_CSV_file input_header_file output_CSV_file"
PROG_DESC = """This program strips the input_CSV_file of all headers not specified in input_header_file \
and writes the result in output_CSV_file"""

PROG_ARGNUM = 3

# import modules
import  sys
import  csv
import  optparse


def  pick_columns(infile, inheader, has_header, outfile, write_hdr):

    # read header file
    with  open(inheader, 'rb') as f_hdr:
        keep_hdr = []
        for  row in f_hdr:
            # strip leading column number if exist
            delimiter = row.find(':')
            if delimiter != -1:
                row = row[delimiter + 1:]
            # create list of headers to keep, not each header could be a num or str
            keep_hdr.append(row.strip('\n\r '))

            if  not has_header and not keep_hdr[-1].isdigit():
                err_str = infile + ' input file must contain headers (-s option) if ' + inheader + \
                    ' header file contains header names'
                raise  ValueError(err_str)

    # read input file
    with  open(outfile, 'ab') as out_f:
        with  open(infile, 'rb') as in_f:
            reader = csv.reader(in_f)
            writer = csv.writer(out_f)

            keep_hdr_int = []
            if  has_header:
                tmp = reader.next() # skip header
                for  needle in keep_hdr:
                    pos = tmp.index(needle) if needle in tmp else -1
                    if  pos != -1:
                        keep_hdr_int.append(pos)

                #  write header if needed
                if write_hdr:
                    tmp_write = []
                    for  i in keep_hdr_int:
                        tmp_write.append(tmp[i])
                    writer.writerow(tmp_write)

            else:
                #  if no header, columns to keep must all be integers, as checked previously
                for  i in keep_hdr:
                    keep_hdr_int.append(int(i) - 1)

            for  row in reader:
                #print  row
                keep_row = []
                # pick out the header columns we want and print it
                for  i in keep_hdr_int:
                    keep_row.append(row[i])
                #print  keep_row
                writer.writerow(keep_row)

    return


def  main():
    parser = optparse.OptionParser(version = '%prog version ' + PROG_VERSION, \
        usage = PROG_USAGE, \
        description = PROG_DESC)
    parser.add_option('-t', '--inheader', help = 'input CSV file has header', \
        dest = 'has_hdr', default = False, action = 'store_true')
    parser.add_option('-o', '--outheader', help = 'write header to output CSV file', \
        dest = 'write_hdr', default = False, action = 'store_true')

    (opts, args) = parser.parse_args()

    if len(args) != PROG_ARGNUM:
        parser.error("incorrect number of arguments!")
    else:
        infile = args[0]
        inheader = args[1]
        outfile = args[2]

    pick_columns(infile, inheader, opts.has_hdr, outfile, opts.write_hdr)

    return

if  __name__ == "__main__":
    main()
