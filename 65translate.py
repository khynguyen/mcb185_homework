#65translate.py by Karen Nguyen 

import argparse 
import mcb185
import sequence

parser =  argparse.ArgumentParser(description='mRNA translator')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100, 
	help='minimum protein length, default: [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', 
	help='also examine the parallel strand')
args = parser.parse_args()

for defline, seq in mcb185.read_fasta(args.file):
	print(defline)
	
	end = False
	for i in range(len(seq) -3 + 1):
		codon = seq[i:i+3]
		if codon == 'ATG':
			aas = []
			for j in range(i, len(seq), 3):
				aa = sequence.trans_ext(seq[j:j+3])
				if aa == '*': 
					end = True
					break
				aas.append(aa)
			protein = ''.join(aas)	
			if len(protein) >= args.min: 
				for k in range(0, len(protein), 60):
						print(protein[k:k+60])
		if end: break
	
	#analyzing parallel stand
	if args.anti: 
		revseq = sequence.revcomp(seq)
		end = False
		for i in range(len(revseq) -3 + 1):
			codon = revseq[i:i+3]
			if codon == 'ATG':
				aas = []
				for j in range(i, len(revseq), 3):
					aa = sequence.trans_ext(revseq[j:j+3])
					if aa == '*': 
						end = True
						break
					aas.append(aa)
				protein = ''.join(aas)	
				print()
				if len(protein) >= args.min:
					for k in range(len(protein), 60):
						print(protein[k:k+60])
			if end: break
