#22fibonacci.py by Karen Nguyen

#function version
def fibonacci(n):
	a = 0
	b = 1
	print(a)
	print(b)
	for i in range(n - 2):
		fibonacci = a + b
		print(fibonacci)
		a = b 
		b = fibonacci

fibonacci(10)

#tuple function version
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

fib(10)

#loop version
a = 0 
b = 1
fibonacci = 0
print(a)
print(b)
for i in range(8):
	fibonacci = a + b
	print(fibonacci)
	a = b 
	b = fibonacci
	
#tuple loop version 
a, b = 0, 1
fib = 0 
for i in range(10):
	print(a)
	a, b = b, a + b