#24savingthrows.py by Karen Nguyen

import random

def advantage():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20) 
	if roll1 > roll2: return roll1 
	return roll2

def disadvantage():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20) 
	if roll1 < roll2: return roll1 
	return roll2
	
trials = 10000
dc = 5

for dc in range(5, 16, 5):
	success = 0
	for i in range(trials):
		roll = random.randint(1, 20)
		if roll >= dc: success += 1
	print(dc, success / trials)
	
for dc in range(5, 16, 5):
	success = 0
	for i in range(trials):
		roll = advantage()
		if roll >= dc: success += 1
	print(dc, success / trials)

for dc in range(5, 16, 5):
	success = 0
	for i in range(trials):
		roll = disadvantage()
		if roll >= dc: success += 1
	print(dc, success / trials)
	
for dc in range(5, 16, 5):
	nor = 0
	adv = 0 
	dis = 0 
	for i in range(trials):
		r1 = random.randint(1,20)
		r2 = random.randint(1,20)
		if r1 >= dc: nor += 1
		if r1 >= dc and r2 >= dc: dis += 1
		if r1 >= dc or r2 >= dc: adv += 1
	print(dc, nor/trials, adv/trials, dis/trials)