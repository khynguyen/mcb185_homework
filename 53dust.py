#53dust.py by Karen Nguyen

import argparse
import mcb185
import math

def entropy(seq):
	h = 0
	comp = []
	comp.append(seq.count('A') / len(seq))
	comp.append(seq.count('C') / len(seq))
	comp.append(seq.count('G') / len(seq))
	comp.append(seq.count('T') / len(seq))
	for nt in comp:
		if nt == 0: continue
		h -= nt * math.log2(nt)
	return h 

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('-w', '--wrap', type=int, default=80,
    help='wrap window size [%(default)i]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()


for defline, seq in mcb185.read_fasta(arg.file):
	masked_seq = list(seq)
	for i in range(len(seq) - arg.size+ 1):
		subseq = seq[i:i + arg.size]
		if entropy(subseq) < arg.entropy: 
			if arg.lower: 
				for j in range(i, i + arg.size): masked_seq[j] = masked_seq[j].lower()
			else: 
				for j in range(i, i + arg.size): masked_seq[j] = 'N'
	print(defline)
	mask = ''.join(masked_seq)
	for i in range(0, len(mask), arg.wrap):
		print(mask[i:i+arg.wrap])