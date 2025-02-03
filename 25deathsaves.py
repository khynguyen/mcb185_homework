#25deathsaves.py by Karen Nguyen 

import random

def deathsaves():
	die = random.randint(1, 20)
	print(die)
	if die == 1:  return 'double failture!'
	elif die == 20: return 'revived!'
	elif die < 10: return 'failure!'
	elif die >= 10: return 'success!'

print(deathsaves())
print(deathsaves())
print(deathsaves())
print(deathsaves())
print(deathsaves())