# Birthday Paradox
import math
import random

l = []

for i in range(50):
  l.append(random.randint(1,365))
# print(l)
# print('after sorting')
l.sort()
print(l)

i = 0 
found = False
while (i < len(l) -1):
  if (l[i] == l[i + 1]):
    found = True
    print('Repeats at', l[i], l[i + 1])
    # break
  i += 1
if (found == False):
  print("Does not Repeat!")