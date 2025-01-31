#12phred.py by Karen Nguyen

import math 

def char_to_prob(x):
	score = ord(x) - 33
	exp = score / 10
	prob = 10**(-exp)
	return prob

print(char_to_prob('!'))
print(char_to_prob(':'))
print(char_to_prob('$'))

def prob_to_char(x):
	if x < 1e-9: return None
	else:
		exp = -math.log10(x)
		score = exp*10 + 33
		char = chr(int(score))
		return char
		
print(prob_to_char(0.005))
print(prob_to_char(0.501))
print(prob_to_char(1e-10))