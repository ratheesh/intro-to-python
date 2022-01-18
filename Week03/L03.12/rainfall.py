# Find the day wise total rainfall for the entered duration of time. eg. week,month etc

days = int(input('Enter no. of days: '))

for i in range(1, days+1):
  total = 0
  rainfall = int(input('Enter the rainfall: '))
  while rainfall != -1:
    total = total + rainfall
    rainfall = int(input('Enter the rainfall: '))
  print(f'Total rainfall of the day {i} is {total}')