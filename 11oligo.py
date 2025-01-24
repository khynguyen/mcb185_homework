#11oligo.py by Karen Nguyen

def oligo_tm(a, c, t, g):
	if a + c + t + g <= 13:
		tm = (a + t)*2 + (g + c)*4
		return tm
	else:
		tm = 64.9 + 41*(g + c - 16.4) / (a + t + c + g)
		return tm

print(oligo_tm(5, 7, 3, 4))
print (oligo_tm(1, 2, 3, 4))
print(oligo_tm(20, 55, 46, 85))