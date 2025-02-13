#32stats.py by Karen Nguyen

import sys 
import math

#add values to list and sort
stats = []
for arg in sys.argv[1:]: 
	f = float(arg)
	stats.append(f)
stats.sort() 

#get median 
middle = len(stats) // 2
if len(stats) % 2 == 0: median = (stats[middle] + stats[middle - 1]) / 2
else: median = stats[middle]

#get length, min, and max
num_values = len(stats)
minimum = stats[0]
maximum = stats[len(stats) - 1] #or stats[-1]

#get mean
total = 0 
for num in stats: total += num
mean = total / num_values

#get sd
sd = 0 
for num in stats: sd += (num - mean) ** 2
sd = math.sqrt(sd / num_values)

#assessment example: N50 calculation
half = total / 2 #from mean calculation
n50 = 0 
for num in stats[::-1]:
	n50 += num 
	if n50 >= half: 
		n50 = num
		break

#printing things in an easy to read way
print('values:', stats)
print('number of values:', num_values)
print('minimum value:', minimum)
print('maxium value:', maximum)
print('mean:', mean)
print('standard deviation:', sd)
print('median value:', median)
print('N50:', n50)