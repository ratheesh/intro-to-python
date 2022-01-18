
num = int(input('Enter a number:'))

factorial = 1

if (num < 0):
  print('Not defined')
else:
  while(num > 0):
    factorial = factorial * (num)
    num = num - 1

  print(factorial)