#54missingkmers.py by Karen Nguyen 

import sys
import mcb185
import itertools
import sequence

none_missing = True #if none missing, keep going
k = 1 #start at kmer length 1 

while none_missing:
	#get kmer count for a certain value of k
	kcounts = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		revseq = sequence.revcomp(seq) #search complementary strand
		for i in range(len(seq) -k + 1):
			kmer_forward = seq[i:i+k]
			kmer_backward = revseq[i:i+k]
			if kmer_forward not in kcounts: kcounts[kmer_forward] = 0
			if kmer_backward not in kcounts: kcounts[kmer_backward] = 0 
			kcounts[kmer_forward] += 1
			kcounts[kmer_backward] += 1
			
	#find missing kmers 
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		if kmer not in kcounts: 
			print(kmer)
			none_missing = False
	
	#increase kmer size until missing kmer found
	k += 1