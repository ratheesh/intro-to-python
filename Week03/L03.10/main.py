# Tutorial on for loop and difference between while loop and for loop

# convert factorial using while loop to for loop

num = int(input('Enter a number: '))
fact = 1

if (num < 1):
  print('Not defined!')
else:
  for i in range(num, 1, -1):
    fact = fact * i

print(fact)