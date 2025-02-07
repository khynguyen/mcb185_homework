#25deathsaves.py by Karen Nguyen 

import random

trial = 10000
revive = 0 
die = 0 
stable = 0

for i in range(trial):
	successes = 0 
	failures = 0 
	for i in range(5):
		roll = random.randint(1, 20)
		if roll == 1: failures += 2
		elif roll < 10: failures += 1 
		elif roll <= 19: successes += 1
		else: 
			revive += 1 
			break
		
		if successes == 3: 
			stable += 1
			break
		if failures >= 3: 
			die += 1
			break
		
print(stable/trial, revive/trial, die/trial)	