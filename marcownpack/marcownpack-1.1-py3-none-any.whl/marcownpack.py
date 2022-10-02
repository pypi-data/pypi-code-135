import argparse
import random
from package import __version__


def main():
    """Entry point
    """
    parser = argparse.ArgumentParser(description='My description')
    parser.add_argument('-v', '--version',
                        help='show the version string and exit',
                        action='store_true')

    args = parser.parse_args()

    if args.version:
        print(parser.prog, __version__)
    else:
        parser.print_usage()

def fact():
    # facts list
    list = ["Seals can fly!", "Birthday's are cool!", "No one asked!", "This is a fact!", "This is a cool package that can give you facts, random variable name, and many more!", "This is not a cool fact ;((((("]
    # random number generator       
    wat = random.randrange(0, len(list))
    # print the fact!
    print(list[wat])    
    # end of function fact()

def varname():
    # variable name list
    list = ["var", "tmp", "temp", "i", "wat", "a", "b", "c", "d", "asghdkjaskjd"]
    wat = random.randrange(0, len(list))
    print(list[wat])
    # end of function varname()
