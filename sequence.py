#sequence.py by Karen Nguyen

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A':   rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: 			rc.append('N')
	return ''.join(rc)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i : i+3]
		if codon == 'ATG':   aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else: 				 aas.append('X')
	return ''.join(aas)

def trans_ext(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i : i+3]
		if codon == 'ATG':   aas.append('M')
		elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA': aas.append('*')
		elif codon == 'TTT' or codon == 'TTC': aas.append('F')
		elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG': aas.append('L')
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA': aas.append('I')
		elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG': aas.append('V') 
		elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG' or codon == 'AGT' or codon == 'AGT': aas.append('S') 
		elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG': aas.append('P') 
		elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG': aas.append('T') 
		elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG': aas.append('A') 
		elif codon == 'TAT' or codon == 'ATC': aas.append('Y') 
		elif codon == 'CAT' or codon == 'CAC': aas.append('H') 
		elif codon == 'CAA' or codon == 'CAG': aas.append('Q') 
		elif codon == 'AAT' or codon == 'AAC': aas.append('N') 
		elif codon == 'AAA' or codon == 'AAG': aas.append('K') 
		elif codon == 'GAT' or codon == 'GAC': aas.append('D') 
		elif codon == 'GAA' or codon == 'GAG': aas.append('E') 
		elif codon == 'TGT' or codon == 'TGC': aas.append('C') 
		elif codon == 'TGG': aas.append('W') 
		elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA'or codon == 'AGG': aas.append('R') 
		elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG': aas.append('G') 
	return ''.join(aas)

def gc_comp(seq):
	gc_count = seq.count('C') + seq.count('G')
	return(gc_count / len(seq))

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def hydrophobicity(aa):
	if aa == 'I': return 4.5 
	if aa == 'V': return 4.2
	if aa == 'L': return 3.8
	if aa == 'F': return 2.8
	if aa == 'C': return 2.5
	if aa == 'M': return 1.9
	if aa == 'A': return 1.8
	if aa == 'G': return -0.4
	if aa == 'T': return -0.7
	if aa == 'S': return -0.8
	if aa == 'W': return -0.9
	if aa == 'Y': return -1.3
	if aa == 'P': return -1.6
	if aa == 'H': return -3.2
	if aa == 'E': return -3.5
	if aa == 'Q': return -3.5
	if aa == 'D': return -3.5
	if aa == 'N': return -3.5
	if aa == 'K': return -3.9
	if aa == 'R': return -4.5

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)

def tm(seq):
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	if a + c + t + g <= 13:
		tm = (a + t)*2 + (g + c)*4
		return tm
	else:
		tm = 64.9 + 41*(g + c - 16.4) / (a + t + c + g)
		return tm