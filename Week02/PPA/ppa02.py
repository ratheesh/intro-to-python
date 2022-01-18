val = float(input())

if (val > 0.0 and val < 10.0):
  print(val + 2.0)
elif (val >= 10.0):
  print((val * val) + 2)
else:
  print(0.0)