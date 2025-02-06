#23triples.py by Karen Nguyen

limit = 101

for a in range(1, limit):
	for b in range(a, limit): 
		c = (a**2 + b**2) ** 0.5 
		if c % 1 == 0: print(a, b, c)

