rollno = int(input())

mod = rollno % 4
if (mod == 1):
  print('Saphire')
elif (mod == 2):
  print('Peridot')
elif (mod == 3):
  print('Ruby')
else:
  print('Emerald')
