#44skew.py by Karen Nguyen

import sequence 

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'

w = 10 
s = 1
subseq = seq[0:w]
gc_
print(sequence.gc_comp(subseq), sequence.gc_skew(subseq))

for i in range(0, len(seq)-w+1, s):
	subseq[]