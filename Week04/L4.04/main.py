import random
l = [3,5,2,5,2524,552,354,5223]
# l = []

for i in range(100000):
  l.append(random.randint(1,10000000))

n = 0
while n > -1:
  found = False
  n = int(input('Enter a number(-1 to exit): '))
  for i in range(len(l)):
    if n == l[i]:
      found = True
      print('Found!')
      break

  if found == False:
    print('Not Found!')


