#55genefinder.py by Karen Nguyen 

##should be 4337 CDS total
##zless GCF_000005845.2_ASM584v2_genomic.gff.gz | cut -f3 | grep 'CDS' | wc

import sys 
import mcb185
import sequence

file = sys.argv[1]
orf_length = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	revseq = sequence.revcomp(seq)
	start_for = 0
	start_rev = 0 
	
	#forward
	for i in range(start_for, len(seq)): 
		codon_for = seq[i:i+3]	
		if codon_for == 'ATG': 	
			for j in range(i, len(seq), 3):
				codon = seq[j:j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					orf = seq[i:j+3]
					if len(orf) < orf_length: 
						start_for = j + 3
						break
					print(orf)
					start_for = j + 3
					break 
	
	#forward
	for i in range(start_rev, len(revseq)): 
		codon_for = revseq[i:i+3]	
		if codon_for == 'ATG': 	
			for j in range(i, len(revseq), 3):
				codon = revseq[j:j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					orf = revseq[i:j+3]
					if len(orf) < orf_length: 
						start_rev = j + 3
						break
					print(orf)
					start_rev = j + 3
					break 