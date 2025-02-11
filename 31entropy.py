#31entropy.py by Karen Nguyen 

import math
import sys

probs = []
for arg in sys.argv[1:]: #for each argument put in the command line
	f = float(arg) #turn into float 
	if f <= 0 or f >= 1: sys.exit('error: not a probability') #only takes valid probs
	probs.append(f) #if valid, add to list 

total = 0
for p in probs: total += p #check to see if probs add up to 1.0
if not math.isclose(total, 1.0): 
	sys.exit('error: probs must sum up to 1.0')

h = 0 
for p in probs:
	h -= p * math.log2(p)

print(f'{h:.4f}')