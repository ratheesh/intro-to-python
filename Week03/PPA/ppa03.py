'''
Accept two positive integers aa and bb as input. Print the sum of all integers in the range [1000,2000], endpoints inclusive, that are divisible by both a and b. If you find no number satisfying this condition in the given range, then print 0.
'''

a = int(input())
b = int(input())

total = 0
count = 0
for x in range(1000, 2001):
  if (x % a == 0 and x % b == 0):
    total += x
    count += 1
print(total)

