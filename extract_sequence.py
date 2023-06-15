from Bio import SeqIO
import sys

record_ids = []
with open(sys.argv[1],'r') as f:
	for line in f:
		raw = line.rstrip().split()
		record_ids.append(raw[0])


seq_dict = {rec.id : rec.seq for rec in SeqIO.parse(sys.argv[2], "fasta")}

for i in record_ids:
	print('>'+i)
	print(seq_dict[i])

