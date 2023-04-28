import functools
import os
import collections
from optparse import OptionParser

def quick_ratio(s1: str, s2: str) -> float:
    """
    Return an upper bound on ratio() relatively quickly.
    https://en.wikipedia.org/wiki/Gestalt_pattern_matching#Applications
    """

    length = len(s1) + len(s2)

    if not length:
        return 1.0

    intersect = collections.Counter(s1) & collections.Counter(s2)
    matches = sum(intersect.values())
    return 2.0 * matches / length

def main(options: dict, args: list) -> float:
    """
    Compare two files or two strings and return a value between 0 and 1
    where 0 means the two files or strings are completely different and
    1 means the two files or strings are identical.

    """
    err = ""
    print(args)
    if len(options.separator) != 1:
        err = "Separator must be one character"
    if options.filename:
        # args[0] is the first file, args[1] is the second file
        if len(args) != 2:
            err = "Please specify two files to compare"
        if args[0] == args[1]:
            err = "The files are the same"
        if not os.path.exists(args[0]):
            err = f"{args[0]} does not exist"
        if not os.path.exists(args[1]):
            err = f"{args[1]} does not exist"
        textA = open(args[0], "r").read()
        textB = open(args[1], "r").read()
    elif options.text: 
        # args[0:-1] is the text but split by a ; 
        if not functools.reduce(lambda acc, x: acc or (options.separator in x), args, False):
            err = f"No separator {options.separator} found in {args}"
        else :
            texts = " ".join(args)
            textA, textB = texts.split(options.separator)
    else:
        err = "Please specify either -f or -t"
    if options.verbose:
        print(f"Text A: {textA}")
        print(f"Text B: {textB}")
    if err == "":
        return quick_ratio(textA, textB), None 
    return None, err

def parse():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", action="store_true", help="Compare two files")
    parser.add_option("-t", "--text", dest="text", action="store_true", default=True, help="Compare two strings, separated by default ';'")
    parser.add_option("-s", "--separator", dest="separator", default=";", help="Separator for text comparison")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true")
    return parser

if __name__ == "__main__":
    parser = parse()
    (options, args) = parser.parse_args()
    res = main(options, args)
    print(res)
