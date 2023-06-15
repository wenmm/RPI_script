from Bio import SeqIO
import sys

with open(sys.argv[2], 'a') as outFile:
	record_ids = list()
	for record in SeqIO.parse(sys.argv[1], 'fasta'):
		if record.id not in record_ids:
			record_ids.append( record.id )
			SeqIO.write(record, outFile, 'fasta')
