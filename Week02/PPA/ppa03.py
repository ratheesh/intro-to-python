time = int(input())

if (time >= 24):
  print('INVALID')
elif (time >= 18):
  print('EVENING')
elif (time >= 12):
  print('AFTERNOON')
elif (time >= 6):
  print('MORNING')
elif (time >=0):
  print('NIGHT')
else:
  print('INVALID')
