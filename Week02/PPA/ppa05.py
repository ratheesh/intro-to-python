
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())

if ((x2 - x1) == 0):
  print('Vertical Line')
else:
  slope = (y2 - y1)/(x2 - x1)
  y3 = (slope * (x3 - x1)) + y1
  print(y3)

  if (slope == 0):
    print('Horizontal Line')
  else:
    if (slope > 0):
      print('Positive Slope')
    else:
      print('Negative Slope')

