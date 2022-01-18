
str = input()

if (len(str) % 2) == 0:
  if (str[-1] == '.'):
    str = str[:-1]
  else:
    str+= '.'

strmid = len(str)//2
print(str[strmid - 1] + str[strmid] + str[strmid + 1])
