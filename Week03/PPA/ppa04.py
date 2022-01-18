n = int(input())

if (n > 2):
  is_prime = True
  for x in range(2, n//2):
    if (n % x == 0):
      is_prime = False
      break

  if (is_prime == True):
    print('PRIME')
  else:
    print('NOTPRIME')
else:
    print('NOTPRIME')
