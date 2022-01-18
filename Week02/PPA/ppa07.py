
str1 = input()
str2 = input()
#str3 = input()
#str4 = input()
#str5 = input()

#if (str1 <= str2) and (str2 <= str3) and (str3 <= str4) and (str4 <= str5):
if (str1 <= str2[str2.index(str1[0]):]):
  print('magical')
else:
  print('non-magical')
