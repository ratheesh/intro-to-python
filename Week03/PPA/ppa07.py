
num = int(input())
total = num % 10
num = num //10
while (num > 0):
  total = total + (num % 10)
  num = num//10

print(total)
