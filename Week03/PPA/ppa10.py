n = int(input())

primesum = 0
num = 2
while num <= n:
  isPrime = True
  for i in range(2, num):
    if (num % i == 0):
      isPrime = False
      break
    else:
      isPrime = True

  if isPrime == True:
    primesum += num
  num += 1

print(primesum)
