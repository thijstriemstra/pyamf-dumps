#!/usr/bin/python
#
# Copyright (c) 2007-2008 The PyAMF Project.
# See LICENSE for details.

"""
Extracts and displays information for files that contain AMF data.
"""

import glob
from optparse import OptionParser
from fnmatch import fnmatch

import pyamf
from pyamf import remoting

def parse_options():
    """
    Parse command-line arguments.
    """
    parser = OptionParser()

    parser.add_option("-d", "--debug", action="store_true", dest="debug",
        default=False, help="Enable debugging")
    parser.add_option("--dump", action="store_true", dest="dump",
        default=False, help="Shows a hexdump of the file")
    parser.add_option("--strict", action="store_true", dest="strict",
        default=False, help="""Option to decode typed but unaliased classes """
        """without raising UnknownClassAlias""")

    return parser.parse_args()

def read_file(fname):
    """
    Read file containing AMF data.
    """
    f = file(fname, "r")
    data = f.read()
    f.close()

    return data

def main():
    """
    Run AMF decoder on input file.
    """
    (options, args) = parse_options()

    print 'Using pyamf from: %s' % (pyamf,)
    print 'Strict = ' + str(options.strict)

    for arg in args:
        for fname in glob.glob(arg):
            if fnmatch(fname, '*.amf*'):
                body = read_file(fname)

                try:
                    print "\nDecoding file:", fname
                    request = remoting.decode(body, None, options.strict)

                    if options.debug:
                        for name, message in request:
                            print "  %s: %s" % (name, message)
                except pyamf.UnknownClassAlias, c:
                    if options.debug:
                        print '\n    Warning: %s' % c
                except pyamf.DecodeError, c:
                    if options.debug:
                        print '\n    Warning: %s' % c
                except:
                    raise

                if options.dump:
                    print
                    print pyamf.util.hexdump(body)

                print "-" * 80

if __name__ == '__main__':
    main()
