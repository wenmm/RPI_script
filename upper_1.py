import sys

with open(sys.argv[1],'r')as f:
	for line in f:
		raw = line.rstrip().split()
		raw[0] = raw[0].upper()
		raw[1] = raw[1].upper()
		print('\t'.join(raw))
