#42ntcomp.py by Karen Nguyen

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	A = 0 
	C = 0
	G = 0 
	T = 0
	N = 0
	length = len(seq)
	for nt in seq:
		if nt == 'A':   A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else: 			N += 1
	print(name, A/length, C/length, G/length, T/length)
	
#using a count list
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	counts = [0, 0, 0, 0, 0] #A, C, G, T, N
	for nt in seq:
		if nt == 'A':   counts[0] += 1
		elif nt == 'C': counts[1] += 1
		elif nt == 'G': counts[2] += 1
		elif nt == 'T': counts[3] += 1
		else: 			counts[4] += 1
	print(name, end=' ')
	for nt in counts:
		print(nt / len(seq), end=' ')
	print()
