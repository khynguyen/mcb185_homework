# 20demo.py by Karen Nguyen

#tuples
t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 26400
print(person)

def mid_point(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2)/ 2
	return x, y
	
m = mid_point(3, 1, 5, 3)
mx, my = mid_point(3, 1, 5, 3)
print(m)
print(m[0], m[1])
print(mx, my)
print(mx)
print(my)

#while loops
i = 0 
while True:
	if i <= 3: 
		print(i)
		i = i + 1
	else: break

i = 0
while i < 5:
	print('hey', i)
	i = i + 1

i = 0
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)