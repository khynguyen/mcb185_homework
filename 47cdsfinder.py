#47cdsfinder.py	by Karen Nguyen

#>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
#ATGCATGCATGCCCCCCCCCCCCCCCCCCCCTAGCTAGCTAG

import sys
import sequence
import mcb185

file = sys.argv[1]
length = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	defwords = defline.split()
	name = defwords[0]
	counts = 1
	
	for i in range(0, len(seq), 3):
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
				print(name, f'#{counts}\n', protein)
				counts += 1
	