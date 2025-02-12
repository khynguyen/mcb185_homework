#35scoringmatrix.py by Karen Nguyen 

import sys 

line = sys.argv[1]
mat = sys.argv[2]
mix = sys.argv[3]

letters = list(line)

#print top line
for let in letters:
	print('  ', let, end='')
print()

for nt1 in letters:
	print(nt1, end=' ')
	for nt2 in letters: 
		if nt2 == nt1: print(mat, end='  ')
		else: print(mix, end='  ')
	print()