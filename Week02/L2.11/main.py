# Different ways to import a library

'''
# Import entire library into the program
import calendar
print(calendar.month(2021, 1))
print(calendar.calendar(2021))

# Import entire library contents into the program
from calendar import *
# print(calendar(2021))
print(month(2021, 2))

# use this if only very few features are used in the importing library
from calendar import month,calendar
print(month(2021, 2))
print(calendar(2022))
'''

# import a library using a different name
import calendar as C
print(C.month(2022, 2))

# or individual method
from calendar import month as m
print(m(2022, 3))