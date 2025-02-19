#test_sequence.py by Karen Nguyen 

import sequence

#transribe and reverse compliment
print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAACGT'))

#translate function
print(sequence.translate('ATGCCCTAA'))

#g_comp and g_skew functions
s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))
