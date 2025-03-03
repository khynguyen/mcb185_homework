#47cdsfinder.py	by Karen Nguyen

import sys
import sequence
import mcb185

file = sys.argv[1]
length = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	defwords = defline.split()
	name = defwords[0]
	
	#forwards
	counts = 1
	for i in range(len(seq)):
		codon = seq[i : i + 3]
		aa = sequence.trans_ext(codon)
		if aa == 'M': 
			protein = 'M'
			for j in range(i + 3, len(seq), 3):
				codon = seq[j: j+3]
				aa = sequence.trans_ext(codon)
				if aa == '*': 
					protein += aa
					break
				protein += aa

			if len(protein) >= length: 
				print(name, f' forward protein #{counts}\n', protein)
				counts += 1
	#backwards
	counts = 1
	for i in range(len(seq), 0, -1):	
		codon = seq[i - 3 : i]
		codon = codon[::-1]
		aa = sequence.trans_ext(codon)
		if aa == 'M': 
			protein = 'M'
			for j in range(i + 3, len(seq), 3):
				codon = seq[j: j+3]
				aa = sequence.trans_ext(codon)
				if aa == '*': 
					protein += aa
					break
				protein += aa

			if len(protein) >= length: 
				print(name, f' backward protein #{counts}\n', protein)
				counts += 1
	