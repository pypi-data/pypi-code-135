
import os
import sys
import argparse

from hash_calc.HashCalc import HashCalc

from carveman.Controller import Controller

jpegHeader = bytearray.fromhex("FFD8FFE0")
jpegFooter = bytearray.fromhex("FFD9")


def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path")
    parser.add_argument("--outdir", "-d", type=str, default="carveman-result", help="The default directory to save carved files")
    args = parser.parse_args()

    if(not os.path.isdir(args.outdir)):
        os.mkdir(args.outdir)

    c = Controller()
    hash = HashCalc(args.path)

    c.printHeader(args.path, args.outdir, hash)

    with open(args.path, "rb") as f:
        data = f.read()
        bA = bytearray(data)

        print("")
        print("--> Carving started")

        _start = 0

        while True:

            start = bA.find(jpegHeader, _start)
            end   = bA.find(jpegFooter, _start+len(jpegHeader))

            if(start == -1):
                break
            else:
                print("")
                print("------> JPEG detected!")
                print("        Found header signature at: " + hex(start) + " Int: " + str(start))
                print("        Found footer signature at: " + hex(end) + " int: " + str(end))
                
    
            img = bytearray()
            for i in range(start, end+len(jpegFooter), 1):
                img.append(data[i])

            file = open(os.path.join(args.outdir, str(hex(start)) + ".jpg"), "wb")
            file.write(img)
            print("        Writing carved .jpg as " + str(hex(start)) + ".jpg")

            _start = end+len(jpegFooter)

    print("")
    print("--> Carving finished")

    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())


# Header: FF D8 FF D0
# Footer: FF D9


# AA AA AA AA BB BB CC DD EE FF XX DD SS DD PP FF | FF D8 FF D0 [File Contnent] FF D9 | AA BB CC DD EE FF GG RR TT EE