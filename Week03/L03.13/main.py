# break continue and pass

# accept the email and print only the user name

# break statement is used the exit the current executing loop
'''
email = input()
for c in email:
  if (c == '@'):
    break
  print(c)
'''

# continue statement
# username in the first line and domain name in the second

# continue statement skip the remaining part of the current executing loop
'''
email = input()
for c in email:
  if (c == '@'):
    print('')
    continue
  print(c, end='')
'''

# pass statement
# problem: task first 10 integers and catogarize into numbers divisible by 3 and 5 respectively and print only 1st catogary

# pass statement is used as a place holder to perform no operation -> null statement
for x in range(11):
  if x % 3 == 0:
    print(x)
  else:
    pass
