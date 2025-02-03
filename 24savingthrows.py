#24savingthrows.py by Karen Nguyen

import random

def saving_throw(dc):
	dice = random.randint(1, 20)
	print(dice)
	if dice >= dc: return 'saved!'
	return 'aww :/'

def advantage(dc):
	dice1 = random.randint(1, 20)
	dice2 = random.randint(1, 20)
	print('dice 1: ', dice1)
	print('dice 2: ', dice2)
	if dice1 > dice2 and dice1 >= dc: return 'saved!'
	elif dice2 >= dice1 and dice2 >= dc: return 'saved!'
	return 'aww :/'

def disadvantage(dc):
	dice1 = random.randint(1, 20)
	dice2 = random.randint(1, 20)
	print('dice 1: ', dice1)
	print('dice 2: ', dice2)
	if dice1 < dice2 and dice1 >= dc: return 'saved!'
	elif dice2 <= dice1 and dice2 >= dc: return 'saved!'
	return 'aww :/'

print(saving_throw(5))
print(saving_throw(10))
print(saving_throw(15))

print(advantage(5))
print(advantage(10))
print(advantage(15))

print(disadvantage(5))
print(disadvantage(10))
print(disadvantage(15))