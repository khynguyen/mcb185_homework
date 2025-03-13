#63kozak.py by Karen Nguyen 

##got help from Catrinel, thanks Cat <3
##kozak sequence: 5'-(gcc)gccRccAUGG-3'

import gzip 
import sys

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'a':   rc.append('t')
		elif nt == 'c': rc.append('g')
		elif nt == 'g': rc.append('c')
		elif nt == 't': rc.append('a')
		else: 			rc.append('N')
	return ''.join(rc)

for_genes = []
rev_genes = [] 
sequence = [] 
get_seq = False #flag to indicate sequence in file

#get sequence and orfs from file
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:	
		f = line.split()
		
		if f[0] == 'CDS':
			cds = f[1]
			if 'complement' in cds:
				if 'join' in cds: continue #COME BACK FOR THIS
				ranges = cds.rstrip().strip('complement(').strip(')').split('..')
				rev_genes.append(ranges)
			else:
				if 'join' in cds: continue #COME BACK FOR THIS
				ranges = cds.rstrip().split('..')
				for_genes.append(ranges)
			 			
		#seq begins after the ORIGIN line
		if line.startswith('ORIGIN'): 
			get_seq = True 
			continue 
		
		#append joined seq lines to sequence list
		if get_seq: 
			if '//' in line: break  #seq ends right before a // line
			frag = ''.join(f[1:]) #skip the position marker at the beginning 
			sequence.append(frag)

#join all the fragments together 
sequence = ''.join(sequence)
revseq = revcomp(sequence)

#get counts for kozak seq 
a = [0] * 15 
c = [0] * 15
g = [0] * 15
t = [0] * 15

for orf in for_genes:
	start = int(orf[0])
	kozak = sequence[start - 8 : start + 7]
	
	for i in range(15):
		if kozak[i] == 'a': a[i] += 1
		elif kozak[i] == 'c': c[i] += 1
		elif kozak[i] == 'g': g[i] += 1
		elif kozak[i] == 't': t[i] += 1

for orf in rev_genes:
	start = int(orf[0])
	kozak = revseq[start - 8 : start + 7]
	
	for i in range(15):
		if kozak[i] == 'a': a[i] += 1
		elif kozak[i] == 'c': c[i] += 1
		elif kozak[i] == 'g': g[i] += 1
		elif kozak[i] == 't': t[i] += 1

	
print(f'{"PO":<8}', 'A   ', 'C   ', 'G   ', 'T   ')		
for i in range(15):
	print(f'{i+1:<8}', a[i], c[i], g[i], t[i])

