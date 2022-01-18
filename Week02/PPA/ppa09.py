

total = int(input())
friend1 = int(input())
friend2 = int(input())
friend3 = int(input())

if ((total == (friend1 + friend2 + friend3)) and (friend1 != 0 and friend2 != 0 and friend3 != 0) and ((friend1 != friend2) and (friend2 != friend3) and (friend1 != friend3))):
  print('FAIR')
else:
  print('UNFAIR')
