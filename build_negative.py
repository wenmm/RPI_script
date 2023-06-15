import sys

RBP = []
with open(sys.argv[1],'r')as f:
	for line in f:
		raw = line.rstrip().split()
		RBP.append(raw[0])

with open(sys.argv[2],'r') as f:
	for line in f:
		a = []
		raw = line.rstrip().split()
		a.append(raw[0].split('-')[0])
		for i in raw[1].split('|'):
			a.append(i.split('-')[0])
		
		for j in RBP:
			if j.split('_')[0] not in a:
				print(raw[0],j.split('_')[0] + '-' + j.split('_')[1])
