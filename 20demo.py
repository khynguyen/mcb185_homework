# 20demo.py by Karen Nguyen

import math

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
	for i in range(n + 1):
		num = (-1) ** i
		denom = (2*i + 2) * (2*i + 3) * (2*i + 4)
		pi = pi + 4* num/denom
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
