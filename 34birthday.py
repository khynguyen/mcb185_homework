#34birthday.py by Karen Nguyen

import random
import sys 

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
matches = 0

for i in range(trials):
	#make a calendar with a zero for each day
	calendar = []
	for i in range(days): calendar.append(0)
	
	#assign every person a birthday
	for person in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1
	
	#see which days have more than 1 person with a birthday
	for date in calendar:
		if date >= 2: 
			matches += 1
			break

prob = matches / trials
print(prob)