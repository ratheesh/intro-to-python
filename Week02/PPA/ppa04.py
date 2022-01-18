x = float(input())
y = float(input())

if (x > 0):
  if (y > 0):
    print('first')
  elif (y < 0):
    print('fourth')
  else:
    print('x-axis')
elif (x < 0):
  if (y > 0):
    print('second')
  elif (y < 0):
    print('third')
  else:
    print('x-axis')
else: # x = 0
  if (y == 0):
    print('origin')
  else:
    print('y-axis')
