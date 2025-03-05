#53dust.py by Karen Nguyen

import argparse
import mcb185
import math

#making all args positional
'''
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('size', type=int, help='window size')
parser.add_argument('entropy', type=float, help='entropy threshold')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''

#making size and entropy named args
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, 
	help='window size [%default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask') #flag
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

#dust program
for defline, seq in mcb185.read_fasta(arg.file):
	print(defline)
	dust = ''
	
	for i in range(len(seq)):
		subseq = seq[i : i + arg.size]
		seq_comp = []
		seq_comp.append(subseq.count('A') / arg.size)
		seq_comp.append(subseq.count('C') / arg.size)
		seq_comp.append(subseq.count('G') / arg.size)
		seq_comp.append(subseq.count('T') / arg.size)
		
		h = 0 
		for p in seq_comp:
			if p == 0: continue
			h -= p * math.log2(p)
		
		if h >= arg.entropy: dust += seq[i]
		elif h < arg.entropy and arg.lower: dust += seq[i].lower()
		else: dust += 'N'
	
	for i in range(0, len(dust) - 60 + 1, 60):
		print(dust[i : i + 60])