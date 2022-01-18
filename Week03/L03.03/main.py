#while to compute Factorial

print('Enter a number:')
n = int(input())

i = 1
ans = 1
while(i <= n):
  ans = ans * i
  i = i + 1

print(ans)