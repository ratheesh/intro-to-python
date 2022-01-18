# count the no. of digits in the number using for loop

'''
num = abs(int(input('Enter a number: ')))
digits = 0

for i in str(num):
  digits = digits + 1

print(digits)
'''

num = int(input())
strnum = str(abs(num))
rev=''

for c in strnum:
  rev = c + rev

if (num < 0):
  rev = '-' + rev

print(rev)
