#66variants.py by Karen Nguyen 

import argparse 
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
args = parser.parse_args()

variants = {}
with gzip.open(args.vcf, 'rt') as fp:
	for line in fp: 
		f = line.rstrip().split()
		if f[0] not in variants: variants[f[0]]= []
		variants[f[0]].append(int(f[1]))
print(variants)

#with gzip.open(args.gff, 'rt') as fp:
	