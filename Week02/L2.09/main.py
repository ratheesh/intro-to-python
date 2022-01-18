# Tutorial on if, else and else if(elif)

# Problem - 1
# Find whether the given number is even or odd

# num = int(input('Enter a number: '))
# if (num % 2 == 0):
#   print("number is even")
# else:
#   print("number is odd")

# Problem - 2
# Find whether the given number ends with 0 or 5 or any other number
# print 0 (for number ending with 0), 5(for number ending with 5) and other if no condition matches

# num = int(input('Enter the number: '))
# if (num % 5 == 0):
#   if(num %10 == 0):
#     print('0')
#   else:
#     print('5')
# else:
#   print('Other')

# Problem 3: Find the grade of student based on the given marks from 0 to 100

# marks = int(input("Enter the Marks: "))
# 
# if (marks >= 0 and marks <= 100):
#   if (marks >= 90):
#     print('A')
#   if (marks >= 80 and marks < 90):
#     print('B')
#   if (marks >=70 and marks < 80):
#     print('C')
#   if (marks >= 60 and marks < 70):
#     print('D')
#   if (marks < 60):
#     print('E')
# else:
#   print('Invalid Input')


# using else if concept
# marks = int(input("Enter the Marks: "))
# if (marks >= 0 and marks <= 100):
#   if (marks >= 90):
#     print('A')
#   elif (marks >= 80):
#     print('B')
#   elif (marks >=70):
#     print('C')
#   elif (marks >= 60):
#     print('D')
#   else:
#     print('E')
# else:
#   print('Invalid Input')

# Problem - 4
# convert flowchart into python
print('Travel from City A to City B')
time = int(input('Enter time: '))
longer = int(input('Define longer: '))

if (time > longer):
  price = int(input('Enter Price: '))
  higher = int(input('Define higher: '))
  if (price >= higher):
    print('Train')
  else:
    print('coach')
else:
  price = int(input('Enter Price: '))
  higher = int(input('Define higher: '))
  if (price >= higher):
    print('Daytime Flight')
  else:
    print('Red Eye Flight')
print('Arrive City B')