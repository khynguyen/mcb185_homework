# 20demo.py by Karen Nguyen

import math
import random

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

#for loops 
for i in range(1, 20, 2): 
	print(i)
	
for i in range(0, 20): 
	print(i)
	
for i in range(5): 
	print(i)

for i in range(1, 20, 2): print(i)
for i in range(0, 20): print(i)
for i in range(5): print(i)

basket = 'eggs', 'milk', 'bread'
for thing in basket:
	print(thing)

for i in range(len(basket)):
	print(basket[i])

#nesting
for i in range(20):
	if i % 2 == 0: print(i, 'is even')
	else: print(i, 'is odd')

#practice problems 
def triangular(n):
	num = 0
	for i in range(n + 1):
		num = num + i
	return num
	
print(triangular(3))
print(triangular(100))

def factorial(n):
	if n == 0: return 1
	num = 1 
	for i in range(1, n + 1):
		num = num * i 
	return num 

print(factorial(4))
print(factorial(12))

def poisson(n, k):
	prob = n**k * math.e**-n / factorial(k)
	return prob

print(poisson(9, 3))

def n_choose_k(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))

print(n_choose_k(8, 3))

def euler(n):
	e = 0
	for i in range(1, n + 1):
		term = i / factorial(i)
		e = e + term
	return e 

print(euler(4))
print(euler(8))
print(euler(17))

def is_prime(n): 
	for i in range(2, n//2):
		if n % i == 0: return False 
	return True 

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(8))
print(is_prime(15))
print(is_prime(31))
	
def estimate_pi(n):
	pi = 3
	for i in range(n):
		num = (-1) ** i
		denom = (2*i + 2) * (2*i + 3) * (2*i + 4)
		pi = pi + 4 * num/denom
	return pi 

def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi

print(estimate_pi(6))
print(estimate_pi(9))
print(estimate_pi(14))

print(nilakantha(6))
print(nilakantha(9))
print(nilakantha(14))

#random numbers 
for i in range(5):
	print(random.random())
	
for i in range(3):
	print(random.randint(1, 6))

#monty pi-thon
total = 0
pi = 0
for i in range(10):
	x = random.random()
	y = random.random()
	distance = (x**2 + y**2) ** 0.5
	if distance < 1: pi += 1
	total += 1
	print(4*pi / total)

#d&d stats - 3D6
total = 0
for i in range(3):
	x = random.randint(1, 6)
	print(x)
	total = total + x

print(total)

#d&d stats - 3D6R1
total = 0
i = 1
while i < 4:
	x = random.randint(1, 6)
	print(x)
	if x == 1: continue
	if x != 1:
		total += x
		i += 1

print(total)

#d&d stats - 3D6x2
total = 0
for i in range(3):
	a = random.randint(1, 6) 
	b = random.randint(1, 6)
	print(a, b)
	if a > b: total += a 
	else: total += b

print(total)

#d&d stats - 4D6d1
total = 0
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)
d = random.randint(1, 6)
print(a, b, c, d)
if a <= b and a <= c and a <= d: total = b + c + d
elif b <= a and b <= c and b <= d: total = a + c + d
elif c <= a and c <= b and c <= d: total = a + b + d
elif d <= a and d <= b and d <= c: total = a + b + c

print(total)

#assessment examples
