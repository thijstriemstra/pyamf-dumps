#!/usr/bin/python
import sys, glob
from optparse import OptionParser

import pyamf

def parse_options():
    parser = OptionParser()

    parser.add_option("-d", "--debug", action="store_true", dest="debug",
        default=False, help="turns debugging on")
    parser.add_option("--dump", action="store_true", dest="dump",
        default=False, help="Shows a hexdump of the file")

    return parser.parse_args()

def read_file(fname):
    f = file(fname, "r")
    data = f.read()
    f.close()

    return data

if __name__ == '__main__':
    (options, args) = parse_options()

    for arg in args:
        for fname in glob.glob(arg):
            data = read_file(fname)
            p = pyamf.AMFMessageDecoder(data)

            if options.debug:
                print "=" * 120

            print "Parsing file:", fname.rsplit("\\",1)[-1]

            try:
                obj = p.decode()
            except:
                raise
            else:
                if options.dump:
                    print pyamf.util.hexdump(data)

                if options.debug:
                    print repr(obj)
