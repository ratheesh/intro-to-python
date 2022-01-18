word = input()

acnt = word.count('a')
ecnt = word.count('e')
icnt = word.count('i')
ocnt = word.count('o')
ucnt = word.count('u')

if ( acnt and ecnt and icnt and ocnt and ucnt):
  if(acnt >= ecnt >= icnt >= ocnt >= ucnt):
    print('It is a perfect word')
  else:
    print('It is not a perfect word')
else:
  print('It is not a perfect word')
