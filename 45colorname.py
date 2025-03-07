#45colorname.py by Karen Nguyen

#colors file formatting: name, hex code, r/g/b

import sys

colorfile = sys.argv[1]
r = int(sys.argv[2])
g = int(sys.argv[3])
b = int(sys.argv[4])

value_diff = 765 #max possible difference to have, 255*3 
color_name = 'blank'

with open(colorfile) as fp:
	for line in fp:
		colors = line.split() #split to get name and values
		color_values = colors[2].split(',') #get just values
		
		R = int(color_values[0]) 
		G = int(color_values[1])
		B = int(color_values[2])
		
		#take total difference
		diff = abs(R - r) + abs(G - g) + abs(B - b)
		#if difference is smaller than prev, get name from first list in line 16
		if diff < value_diff: 
			value_diff = diff
			color_name = colors[0] 
			value = colors[2] 

print(color_name, value, value_diff, sep='    ')	