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

#compare the letters
for nt1 in letters:
	print(nt1, end=' ')
	for nt2 in letters: 
		if nt2 == nt1: print(mat, end='  ')
		else: print(mix, end='  ')
	print()

#alternatively, using formatted strings
#can't get this solution to look as lined up as the first one tho 
line = sys.argv[1]
mat = sys.argv[2]
mix = sys.argv[3]

letters = list(line)

#print top line
for let in letters:
	print(f'{let:>4}', end='')
print()

#compare the letters
for nt1 in letters:
	print(nt1, end='')
	for nt2 in letters: 
		if nt2 == nt1: print(f'{mat:>4}', end='')
		else: print(f'{mix:>4}', end='')
	print()