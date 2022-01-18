
maxNo = 0
while True:
  num = int(input())
  if (num == 0):
    print(maxNo)
    break
  else:
    if (num > maxNo):
      maxNo = num
