#!/usr/bin/python

import sys, getopt

def usage():
	print 'Usage: sav-to-srm.py -i <input.sav> -o <output.srm> [--byteswap]'
	print 'Converts GBA SAV files to RetroArch SRM format'

def main(argv):
	inputfile = None
	outputfile = None
	byteswap = None

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["input=","output=","byteswap"])
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

		for i in xrange(139264 - len(data)):
			outfile.write(chr(255))
		
		if byteswap:
			for i in xrange(len(data) / 8):
				outfile.write(data[i*8+7])
				outfile.write(data[i*8+6])
				outfile.write(data[i*8+5])
				outfile.write(data[i*8+4])
				outfile.write(data[i*8+3])
				outfile.write(data[i*8+2])
				outfile.write(data[i*8+1])
				outfile.write(data[i*8])
		else:
			outfile.write(data)
			
		print "Inserted", len(data), "bytes from", inputfile, "to", outputfile

if __name__ == "__main__":
	main(sys.argv[1:])
