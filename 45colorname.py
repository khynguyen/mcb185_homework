#45colorname.py by Karen Nguyen

#colors_extended are formatted as (name \t hex code \t r,g,b)

import sys

colorfile = sys.argv[1]
r = int(sys.argv[2])
g = int(sys.argv[3])
b = int(sys.argv[4])

value_diff = 765 #max possible difference to have, 255*3 

with open(colorfile, 'rt') as fp:
	for line in fp:
		colors = line.split()
		color_values = colors[2].split(',')
		
		R = int(color_values[0])
		G = int(color_values[1])
		B = int(color_values[2])
		
		diff = abs(R - r) + abs(G - g) + abs(B - b)
		if diff < value_diff: 
			value_diff = diff
			color_name = colors[0]

print(color_name)