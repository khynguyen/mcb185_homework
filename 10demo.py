#10demo.py by Karen Nguyen

#printing practice
import math

print('hello, again')
print("""
This that pretty girl mantra
this that flaunt ya
Just touched down in LA
""")

#math functions
print(1.5e-2)
print('143 // 10 =', 143 // 10)
print('143 % 10 =', 143 % 10)
print(2**3)
print(pow(2, 3))
print(math.log10(1000))
print(math.factorial(4))
print(round(math.pi, ndigits=5))

#pythagorean theorem many ways
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b):
	c = (a**2 + b**2) ** 0.5
	return c

hyp = pythagoras(3, 4)
print(hyp)

def pythagoras2(a, b):
        return math.sqrt(a**2 + b**2)

print(pythagoras2(3, 4))

def pythagoras3(a, b): return math.sqrt(a**2 + b**2)
print(pythagoras3(3, 4))

#practice with functions
def circle_area(r):
	area = math.pi * (r**2)
	return r

def rectangle_area(w, h): return w * h

def triangle_area(w, h):
	area = rectangle_area(w, h) * 0.5
	return area

print(circle_area(3))
print(rectangle_area(3, 5))
print(triangle_area(3,5))

def f2c(f): return (32 - f) * 5/9
print(f2c(98.6))

def m2k(m): return m * 0.62
print(m2k(1000))

def dna_conc(od, df): return od * df * 50
print(dna_conc(2, 6))
#strings
s = 'hello world'
print(s)

#conditionals
a = 3
b = 3
if a == b:
	print('a equals b')
	
c = 4
d = 5
if c == d:
	print('c equals d')
else:
	print('c does not equal d')

def is_even(x):
	if x % 2 == 0: 
		return True
	else:
		return False

print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a < b: 	print('a < b')
elif a > b: print('a > b')
else: 		print('a == b')

if   a < b:  print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!')

e = 103
f = 98

if e > 50 and e < 100: print('yay')
else: print('*sad*')

if f > 50 and f < 100: print('yay')
else: print('*sad*')

#floating point numbers
a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

#a = 1
#s = 'G'
#if a < s: print('a < s')

def oops(m, x, b):
	y = m * x + b
	
print(oops(2, 3, 4))

#more practice
def is_integer(x):
	if x % 1 == 0: return True
	else: return False

print(is_integer(3))
print(is_integer(3.14))

def valid_prob(x):
	if x >= 0 and x <= 1: return 'valid probability'
	else: return 'invalid probability' 
	
print(valid_prob(0.75))
print(valid_prob(2))

def base_weight(x):
	if x == 'A' or x == 'a': return '135.13 g/mol'
	elif x == 'T' or x == 't': return '126.1133 g/mol'
	elif x == 'C' or x == 'c': return '111.1 g/mol'
	elif x ==  'G' or x == 'g': return '151.13 g/mol'
	else: return None

print(base_weight('A'))
print(base_weight('t'))
print(base_weight('c'))
print(base_weight('G'))
print(base_weight('f'))

def base_complement(x):
	if x == 'A' or x == 'a': return 'T'
	elif x == 'T' or x == 't': return 'A'
	elif x == 'C' or x == 'c': return 'G'
	elif x ==  'G' or x == 'g': return 'C'
	else: return None

print(base_complement('A'))
print(base_complement('t'))
print(base_complement('c'))
print(base_complement('G'))
print(base_complement('f'))

#even more practice
def max_num(a, b, c):
	if a - b > 0 and a - c > 0: return a
	elif b - a > 0 and b - c > 0: return b
	elif c - a > 0 and c - b > 0: return c

print(max_num(1, 2, 3))

def sensitivity(tp, fn):
	sen = tp / (tp + fn)
	return sen 
	
def specificity(tn, fp):
	spec = tn / (tn + fp)
	return spec
	
def f1_score(tp, fp, fn):
	f1 = tp / (tp + 0.5 * (fp + fn))
	return f1
	
print(sensitivity(.92, .08))
print(specificity(.97, .03))
print(f1_score(.92, .03, .08))

def shannon_entropy(a, c, t, g):
	if a == 0: 	a = 0
	else: 		a = a * math.log2(a)
	if c == 0:  c = 0
	else: 		c = c * math.log2(c)
	if t == 0:  t = 0
	else: 		t = t * math.log2(t)
	if g == 0:  g = 0
	else: 		g = g * math.log2(g)
	return a + c + t + g
	
print(shannon_entropy(0.25, 0.25, 0.25, 0.25))
print(shannon_entropy(0, 0, 0.5, 0.5))

#assessment examples
def distance(x1, y1, x2, y2):
	d = ((x2 - x1)**2 + (y2 -y1)**2)**0.5
	return d
	
print(distance(2, 3, 5, 6)) #points (2, 3) and (5, 6)

def base_complement(x):
	if x == 'A' or x == 'a': return 'T'
	elif x == 'T' or x == 't': return 'A'
	elif x == 'C' or x == 'c': return 'G'
	elif x ==  'G' or x == 'g': return 'C'
	else: return None

print(base_complement('A'))
print(base_complement('t'))
print(base_complement('c'))
print(base_complement('G'))
print(base_complement('f'))

def max3(a, b, c):
	if a - b > 0 and a - c > 0: return a
	elif b - a > 0 and b - c > 0: return b
	elif c - a > 0 and c - b > 0: return c

print(max3(19, 38, 52))