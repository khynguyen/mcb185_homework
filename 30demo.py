#30demo.py by Karen Nguyen

import math
import sys

#strings 
s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

s = 'hello' + 'world'
print(s)

polyA = "A" * 100
print(polyA)

print('A' < 'B')
print('A' < 'a')
print('1' < '10')
print('100' < '2')

#string functions
print(len('hello world'))

print(chr(60))

print(ord('A'))

#method syntax
print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))
print(s)

#string formatting
a = 1/3

print(f'{math.pi:.3f}')
print(f'{math.pi:.5f}')
print(f'{a:.5f}')

print(f'{1e6 * math.pi:e}')
print(f'{2 * math.pi:e}')
print(f'{1e5 * a:e}')

print(f'{"hello world":>20}')
print(f'{"hello world":>40}')
print(f'{"wassupppppp":>30}')

print(f'{"hello world":.>20}')
print(f'{"hello world":&>20}')
print(f'{"over here!":_>45}')

print(f'{20:<10} {10}')
print(f'{20:<30} {10}')
print(f'{"hi":<25} {"there"}')

print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))

#indexes
seq = 'GAATTC'
print(seq[0], seq[1], seq[4])
print(seq[-1], seq[-2])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
#slices
s = 'ABCDEFGHIJK'
print(s)
print(s[0:5])
print(s[0:11:2])

print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1])

dna = 'ATCGATCGATACGGC'
for i in range(0, len(dna), 3):
	codon = dna[i: i+3]
	print(codon)
	
#tuples
tax = ('homo', 'sapiens', 9606)
print(tax)

#dna[0] = 'C'
#tax[0] = 'human'

print(tax[0])
print(tax[::-1])

#enumerate() and zip()
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

one_letter = 'ACDEFGHIKLMNPQRSTVWY'
thr_letter = ('ala', 'cys', 'asp', 'glu', 'phe', 'gly', 'his', 'ile', 'lys', 'leu', 'met', 'asn', 'pro', 'gln', 'arg', 'ser', 'thr', 'val', 'trp', 'tyr')

for i in range(len(one_letter)):
	print(one_letter[i], thr_letter[i])

for one, thr in zip(one_letter, thr_letter):
	print(one, thr)

#lists
nts = ['A', 'T', 'C']
print(nts)

nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)
print(nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

nucleotides = nts.copy()
print(nts, nucleotides)

nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)
stuff.append(5)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day 		to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)
print(aas)

#searching 
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
 #print('index Z?', alph.index('Z'))
 
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

#practice problems
list1 = [ 5, 10, 3, 2, 55, 24, 46, 23]
list2 = ['c', 'H', 't', 'P', 'a', 'Q']

def minimum(lst):
	minimum = lst[0]
	for item in lst[1:]:
		if item < minimum: minimum = item
	return minimum

print(minimum(list1))
print(minimum(list2))

def min_max(lst):
	minimum = lst[0]
	maximum = lst[0]
	for item in lst[1:]:
		if item < minimum: minimum = item
		if item > maximum: maximum = item
	return minimum, maximum

print(min_max(list1))
print(min_max(list2))

def mean(lst):
	total = 0
	for item in lst: total += item
	return total / len(lst)

print(mean(list1))

def entropy(probs):
	h = 0
	for p in probs:
		if p == 0: h = h
		h -= p * math.log2(p)
	return h 

print(entropy([0.1, 0.3, 0.5, 0.1]))
print(entropy([0.2, 0.3, 0.5]))

def kullback(list1, list2):
	d = 0 
	for p1, p2 in zip(list1, list2):
		d += p1 * math.log2(p1 / p2)
	return d 

p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)

print(kullback(p1, p2))

#command line data 
#remember to import sys 
print(sys.argv)

#converting types
i = int(42)
x = float('0.61385')
print(i * x)

print(type(i), type(x), type(i * x))

#assessment example
dna = 'ATGCTGTAA'
	
nts = list(dna)

for i in range(1, len(nts) + 1):
	frame = 0 
	if i % 3 == 0: frame = 3
	elif (i + 1) % 3 == 0: frame = 2
	else: frame = 1
	
	codon = nts[i - 1: i + 2]
	codon = ''.join(codon)
	if len(codon) < 3: break
	
	print(i, frame, codon)
