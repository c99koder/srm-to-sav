#!/usr/bin/python

import sys, getopt


def usage():
    print('Usage: srm-to-sav.py -i <input.srm> -o <output.sav> [--byteswap]')
    print('Converts RetroArch SRM files to raw GBA SAV format')


def main(argv):
    inputfile = None
    outputfile = None
    byteswap = None

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output=", "byteswap"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt == "--byteswap":
            byteswap = True

    if (not inputfile or not outputfile):
        usage()
        sys.exit(2)

    with open(inputfile, "rb") as infile, open(outputfile, "wb") as outfile:

        data = infile.read()
        # Limit size of file to .sav length
        data = data[:131072]

        if byteswap:
            for i in range(int(len(data) / 8)):
                outfile.write(data[i * 8 + 7])
                outfile.write(data[i * 8 + 6])
                outfile.write(data[i * 8 + 5])
                outfile.write(data[i * 8 + 4])
                outfile.write(data[i * 8 + 3])
                outfile.write(data[i * 8 + 2])
                outfile.write(data[i * 8 + 1])
                outfile.write(data[i * 8])
        else:
            outfile.write(data)

        print("Extracted", len(data), "bytes from", inputfile, "to", outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
