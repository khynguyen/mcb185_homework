#48transmembrane.py by Karen Nguyen

import sys 
import mcb185
import sequence

file = sys.argv[1]

for defline, seq in mcb185.read_fasta(file):
	#skip super short proteins 
	if len(seq) < 41: continue
	
	#find signal peptide in first 30 amino acids
	for i in range(30):
		signal = seq[i:i+8]
		if 'P' in signal: continue
		kd = 0 
		for aa in signal:
			kd += sequence.hydrophobicity(aa)
		
		#if we find a signal sequence, find transmembrane sequence
		transmembrane = False
		if kd / 8 >= 2.5:
			for j in range(31, len(seq)):
				region = seq[j:j+11]
				if 'P' in region: continue
				kd = 0 
				for aa in region:
					kd += sequence.hydrophobicity(aa)
				if kd / 11 >= 2.0:
					print(defline)
					transmembrane = True
					break
		if transmembrane: break