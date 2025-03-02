#44skew.py by Karen Nguyen

import sequence 
import sys 
import mcb185
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	w = int(sys.argv[2])
	s = 1
	subseq = seq[0:w]

	c = subseq.count('C')
	g = subseq.count('G')
	print(0, sequence.gc_comp(subseq), sequence.gc_skew(subseq))

	for i in range(0, len(seq)-w , s):
		if   seq[i + w] == 'G': g += 1
		elif seq[i + w] == 'C': c += 1
		
		if   seq[i] == 'G': g -= 1
		elif seq[i] == 'C': c -= 1
		
		comp = (g + c) / w
		skew = (g - c) / (g + c)
		print(i + 1, g + c, comp, skew)