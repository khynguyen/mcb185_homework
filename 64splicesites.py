#64splicesites.py by Karen Nguyen 

import mcb185
import sys 
import gzip

fasta = sys.argv[1]
gff = sys.argv[2]

donor_sites = {}
acceptor_sites = {}

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
		if f[2] == 'intron': 
			if f[0] not in donor_sites: donor_sites[f[0]] = []
			if f[0] not in acceptor_sites: acceptor_sites[f[0]] = []
			donor_sites[f[0]].append(int(f[3]))
			acceptor_sites[f[0]].append(int(f[4]))

for defline, seq in mcb185.read_fasta(fasta):
	defwords = defline.strip('>').split()
	chrom = defwords[0]
	if chrom == 'MtDNA': continue
	
	for acceptor in acceptor_sites[chrom]:
		site = seq[acceptor - 7: acceptor]
		for i in range(len(site)):
			if site[i] == 'A': A_acc[i] += 1
			elif site[i] == 'C': C_acc[i] += 1
			elif site[i] == 'G': G_acc[i] += 1
			elif site[i] == 'T': T_acc[i] += 1
	
	for donor in donor_sites[chrom]:
		site = seq[donor - 1: donor + 6]
		for i in range(len(site)):
			if site[i] == 'A': A_don[i] += 1
			elif site[i] == 'C': C_don[i] += 1
			elif site[i] == 'G': G_don[i] += 1
			elif site[i] == 'T': T_don[i] += 1

print('AC DEMO1', 'XX', 'ID ACC', 'XX', 'DE Splice Acceptor', sep='\n')
for i in range(7):
	print(f'{i+1:<8}', f'{A_acc[i]: <8}', f'{C_acc[i]: <8}', f'{G_acc[i]: <8}', f'{T_acc[i]: <8}')

print('AC DEMO2', 'XX', 'ID DON', 'XX', 'DE Splice Donor', sep='\n')
for i in range(7):
	print(f'{i+1:<8}', f'{A_don[i]: <8}', f'{C_don[i]: <8}', f'{G_don[i]: <8}', f'{T_don[i]: <8}')