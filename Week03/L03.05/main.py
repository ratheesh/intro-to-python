# Introduction to for loop

# for i in range(10):
#   print(i, 'Hello India')
#   print('**************')


n = int(input('Enter a Number: '))
for i in range(n):
  if (i % 2) == 0:
    print(i, 'Hello India')
  else:
    print(i, "Hi World")
    