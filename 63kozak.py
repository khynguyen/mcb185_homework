#63kozak.py by Karen Nguyen 

import gzip 
import sys

#adjusted revcomp function to work on lowercase characters
def revcomp(dna):
	rc = []
	for nt in dna:
		if nt == 'a':   rc.append('t')
		elif nt == 'c': rc.append('g')
		elif nt == 'g': rc.append('c')
		elif nt == 't': rc.append('a')
		else: 			rc.append('N')
	return ''.join(rc)

#get seq and orfs
for_genes = []
rev_genes = []
seq_frags = []
get_seq = False

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		
		#get positions of cds 
		if f[0] == 'CDS':
			if 'complement' in f[1]: 
				cds = f[1].strip('complement(').strip(')')
				rev_genes.append(cds)
			else: for_genes.append(f[1])
		
		#sequence begins after ORIGIN, set flag to True
		if line.startswith('ORIGIN'): 
			get_seq = True
			continue
		
		#once True, put seq fragments into list	
		if get_seq:
			seq = ''.join(f[1:])
			seq_frags.append(seq)

#get string of both dna strands
sequence = ''.join(seq_frags)
revseq = revcomp(sequence)

#nt counting
A = [0] * 15
C = [0] * 15
G = [0] * 15
T = [0] * 15

for frame in for_genes:
	if 'join' in frame:
		sections =  frame.strip('join(').strip(')').split(',')
		beg, end = sections[0].split('..')
		start = int(beg)
		kozak = sequence[start - 8 : start + 7]

		for i in range(15):
			if kozak[i] == 'a': A[i] += 1
			elif kozak[i] == 'c': C[i] += 1
			elif kozak[i] == 'g': G[i] += 1
			elif kozak[i] == 't': T[i] += 1
			
	else: 
		beg, end = frame.split('..')
		start = int(beg)
		kozak = sequence[start - 8 : start + 7]
		for i in range(15):
			if kozak[i] == 'a': A[i] += 1
			elif kozak[i] == 'c': C[i] += 1
			elif kozak[i] == 'g': G[i] += 1
			elif kozak[i] == 't': T[i] += 1
			
for frame in rev_genes:
	if 'join' in frame:
		sections =  frame.strip('join(').split(',')
		beg, end = sections[0].split('..')
		start = int(end)
		kozak = revseq[start - 8 : start + 7]

		for i in range(15):
			if kozak[i] == 'a': A[i] += 1
			elif kozak[i] == 'c': C[i] += 1
			elif kozak[i] == 'g': G[i] += 1
			elif kozak[i] == 't': T[i] += 1
			
	else: 
		beg, end = frame.split('..')
		start = int(end)
		kozak = revseq[start - 8 : start + 7]
		kozak = kozak[::-1]
		#print(kozak)
		for i in range(15):
			if kozak[i] == 'a': A[i] += 1
			elif kozak[i] == 'c': C[i] += 1
			elif kozak[i] == 'g': G[i] += 1
			elif kozak[i] == 't': T[i] += 1


print('KOZAK SEQ NT COUNTS', 'XX', 'ID ECOLI', 'XX', sep='\n')
print(f'{"PO":<8}', f'{"A": <8}', f'{"C": <8}', f'{"G": <8}', f'{"T": <8}')

for i in range(15):
	print(f'{i+1:<8}', f'{A[i]: <8}', f'{C[i]: <8}', f'{G[i]: <8}', f'{T[i]: <8}')