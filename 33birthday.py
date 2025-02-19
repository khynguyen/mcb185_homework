#33birthday.py by Karen Nguyen

import random
import sys 

random.seed(9)

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
matches = 0

#solution i did on my own
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

#solution 1 done in class 2/18
random.seed(9)
matches = 0
for i in range(trials):
	birthdays = []
	for i in range(people):
		birthdays.append(random.randint(0, days))
	
	stop = False
	for i in range(len(birthdays)):
		for j in range(i + 1, len(birthdays)):
			if birthdays[i] == birthdays[j]: 
				matches += 1
				stop = True
				break 
		if stop: break

prob = matches / trials 
print(prob)

#solution 2 done in class 2/18
#more efficient but it doesn't seem to give me the same number as the first 2
random.seed(9)
matches = 0
for i in range(trials):
	birthdays = []
	for i in range(people):
		bday = random.randint(0, days - 1)
		if bday in birthdays: 
			matches += 1
			break
		else: birthdays.append(bday)
	
print(matches / trials)