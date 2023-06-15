import sys

rna_rbp = {}
with open(sys.argv[1],'r') as f:
	for line in f:
		raw = line.rstrip().split()
		rna_rbp.setdefault(raw[1].upper(),[]).append(raw[0].upper())	



for k,v in rna_rbp.items():
	print(k,'|'.join(list(set(v))), len(list(set(v))))
