passwd = input()

if (len(passwd) < 8 or len(passwd) > 32):
  print('False')
elif (not passwd[0].isalpha()):
  print('False')
elif (passwd.count('/') or passwd.count('\\') or passwd.count('=') or passwd.count("'") or passwd.count('"') or (passwd.count(' '))):
  print('False')
else:
  print('True')
