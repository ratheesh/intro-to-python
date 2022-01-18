# Introduction to import library
import math
import random

print(math.log(10))
print(math.sqrt(9))
print(math.factorial(5))

print(random.random())

print('-----------------------')

#coin toss game
# a = random.random()
# if (a < 0.5):
#   print('Heads')
# else:
#   print('Tails')

# 6-faced dice
# print(random.randrange(1,7))

dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)
total = dice1 + dice2
print('you pair of dice is', total)