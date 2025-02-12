#33birthday.py by Karen Nguyen

import random
import sys 

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
matches = 0

for i in range(trials):
	#make birthdays list and add birthdays
	birthdays = []
	for person in range(people):
		birthdays.append(random.randint(0, days))
	
	#iterate through each combination to see if birthdays match
	#break out of both loops the moment we get a match
	for p1 in birthdays:
		stop = False
		for p2 in birthdays[birthdays.index(p1) + 1:]:
			if p1 == p2: 
				matches += 1
				stop = True
				break 
		if stop: break

prob = matches / trials 
print(prob)