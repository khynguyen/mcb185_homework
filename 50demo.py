#50demo.py by Karen Nguyen

import random
import sys
import itertools #see line 104

#demo in class 3/4/2025
'''
for i in range(1000):
	name = random.choices('ABCDEFGHIJKLMNOP', k=7)
	name = ''.join(name)
	val = random.random()
	print(name, val)

#this became data.txt

names = []
vals = []
with open(sys.argv[1]) as fp:
	for line in fp:
		name, val = line.split()
		names.append(name)
		vals.append(val)

print(names[:3])
print(vals[:3])

if 'DEACAAK' in names:
	pos = names.index('DEACAAK')
	print(vals[pos])

#essentially trying to show us what we do if we didn't have a dictionary
and why dictionaries are useful
'''

#sets
s = {'A', 'C', 'G'}
print(s)

s.add('T')
print(s)

s.add('A')
print(s)

##print(s[2]) <- gives an error, sets do not have indices

#dictionaries 
d = {}
d = dict()
print(d, type(d))

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

##print(d['rat']) <- gives error, not in the dictionary yet

if 'dog' in d: print(d['dog'])

#iterating with dictionaries
for key in d: print(f'{key} says {d[key]}')

for key, value in d.items(): print(key, 'says', value)
for key, value in d.items(): print(f'{key} says {value}')

##don't do this, ALWAYS UNPACK INSTEAD
for thing in d.items(): print(thing[0], 'says', thing[1]) 

print(d.keys())
print(d.values())
print(list(d.values()))

#lookup tables
kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)

print(kd_dict('IVIVIV'))
print(kd_dict('MANSKDQPDMKWSDWI'))

#alternative to 42ntcomp.py 
'''
count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1
'''

#use itertools to find all possible combinations 
for nts in itertools.product('ACGT', repeat=2): 
	print(nts)