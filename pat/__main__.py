"""Python cAT

A cat replacement written in python.
"""

from argparse import ArgumentParser

from . import PyCat, VERSION

def pat_arguments():
    """Configure an Argument parser and return a Namespace of
    arguments for pat.
    """
    parser = ArgumentParser()
    
    parser.add_argument("-n", "--number",
                        action="store_true",
                        help="Number all output lines")
    
    parser.add_argument("-b", "--non-blank",
                        action="store_true",
                        help="Number non-blank lines, overrides number")
    
    parser.add_argument("-E","--show-ends",
                        action="store_true",
                        help="Appends a $ to the end of each line")

    parser.add_argument("-T","--show-tabs",
                        action="store_true",
                        help="Tabs are written as ^I");
    
    parser.add_argument("-v","--version",
                        action="store_true",
                        help="");
    
    parser.add_argument("FILE", nargs="*")
    
    args = parser.parse_args()
        
    return args


def main():
    """pat
    """

    args = pat_arguments()

    if args.version:
        print(f"pcat version {VERSION}")
        exit(0)

    pycat = PyCat(args.FILE, args.number, args.non_blank, args.show_ends, args.show_tabs)
    
    pycat()
    
