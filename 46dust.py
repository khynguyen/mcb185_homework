#46dust.py by Karen Nguyen

import sys
import mcb185
import math

file = sys.argv[1]
w = int(sys.argv[2]) 
e = float(sys.argv[3]) 

for defline, seq in mcb185.read_fasta(file):
	print(defline)
	dust = ''
	
	for i in range(len(seq)):
		subseq = seq[i : i + w]
		seq_comp = []
		seq_comp.append(subseq.count('A') / w)
		seq_comp.append(subseq.count('C') / w)
		seq_comp.append(subseq.count('G') / w)
		seq_comp.append(subseq.count('T') / w)
		
		h = 0 
		for p in seq_comp:
			if p == 0: continue
			h -= p * math.log2(p)
		
		if h >= e: dust += seq[i]
		else: 	   dust += 'N'
	
	for i in range(0, len(dust) - 60 + 1, 60):
		print(dust[i : i + 60])