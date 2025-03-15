#!/usr/bin/env python3
#64splicesites.py by Karen Nguyen 

import mcb185
import sys 
import gzip

def comp(dna):
	rc = []
	for nt in dna:
		if nt == 'A':   rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: 			rc.append('N')
	return ''.join(rc)

fasta = sys.argv[1]
gff = sys.argv[2]

splice_sites = {}

A_acc = [0] * 7
C_acc = [0] * 7
G_acc = [0] * 7
T_acc = [0] * 7

A_don = [0] * 7
C_don = [0] * 7
G_don = [0] * 7
T_don = [0] * 7

with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.rstrip().split()
		if f[1] == 'RNASeq_splice': 
			if f[0] not in splice_sites: splice_sites[f[0]] = []
			sites = int(f[3]), int(f[4]), f[6]
			splice_sites[f[0]].append(sites)

for defline, seq in mcb185.read_fasta(fasta):
	defwords = defline.strip('>').split()
	chrom = defwords[0]
	if chrom == 'MtDNA': continue
	revseq = comp(seq)
	
	for sites in splice_sites[chrom]:
		donor, acceptor, strand = sites
		if sites[2] == '+':
			acc_site = seq[acceptor - 7: acceptor]
			don_site = seq[donor - 1: donor + 6]
		else: 
			acc_site = revseq[acceptor - 7: acceptor]
			don_site = revseq[donor - 1: donor + 6]
		
		for i in range(7):
			if acc_site[i] == 'A': A_acc[i] += 1
			elif acc_site[i] == 'C': C_acc[i] += 1
			elif acc_site[i] == 'G': G_acc[i] += 1
			elif acc_site[i] == 'T': T_acc[i] += 1	
		
			if don_site[i] == 'A': A_don[i] += 1
			elif don_site[i] == 'C': C_don[i] += 1
			elif don_site[i] == 'G': G_don[i] += 1
			elif don_site[i] == 'T': T_don[i] += 1

print('AC DEMO1', 'XX', 'ID ACC', 'XX', 'DE Splice Acceptor', sep='\n')
for i in range(7):
	print(f'{i+1:<8}', f'{A_acc[i]: <8}', f'{C_acc[i]: <8}', f'{G_acc[i]: <8}', f'{T_acc[i]: <8}')

print('AC DEMO2', 'XX', 'ID DON', 'XX', 'DE Splice Donor', sep='\n')
for i in range(7):
	print(f'{i+1:<8}', f'{A_don[i]: <8}', f'{C_don[i]: <8}', f'{G_don[i]: <8}', f'{T_don[i]: <8}')