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

for key, value in variants.items():
	for var in value:
		regions = []
		with gzip.open(args.gff, 'rt') as fp:
			for line in fp: 
				f = line.rstrip().split()
				region = f[2]
				beg = int(f[3])
				end = int(f[4])
				
				if beg > var: break
				if var > beg and var < end and region not in regions:
					regions.append(region)
		if regions == []: continue
		regions = ', '.join(regions)
		print(key, var, regions, sep='\t')