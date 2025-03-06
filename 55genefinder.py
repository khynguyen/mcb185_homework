#55genefinder.py by Karen Nguyen 

##should be ~4337 CDS total
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
		codon_for = seq[start_for:start_for+3]	
		
		#if start codon, find stop codon by going by 3's
		if codon_for == 'ATG': 	
			for j in range(start_for, len(seq), 3):
				codon = seq[j:j+3]
				
				#if stop codon, get coordinates of orf 
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					orf = seq[start_for:j+3]
					if len(orf) < orf_length:  #if too short, move on
						start_for = j + 3
						break
						
					beg = start_for + 1
					end = j + 3 
					print('+', beg, end)
					start_for = j + 3
					break 
		
		start_for += 1
	
	
	#backwards
	for i in range(start_rev, len(revseq)): 
		codon_rev = revseq[start_rev:start_rev+3]	
		
		#if start codon, find stop codon by going by 3's
		if codon_rev == 'ATG': 	
			for j in range(start_rev, len(revseq), 3):
				codon = revseq[j:j+3]
				
				#if stop codon, get coordinates of orf
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					orf = revseq[start_rev:j+3]
					if len(orf) < orf_length: #if too short, move on
						start_rev = j + 3
						break
					
					beg = len(seq) - j - 2
					end = len(seq) - start_rev 
					print('-', beg, end) 
					start_rev = j + 3
					break 
		start_rev += 1
