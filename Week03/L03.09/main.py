# Formatted printing
# sep: def: Space
# end: def: CR

'''
#print without carriage return
for x in range(10):
  print(x, end = '') # end with env param

d = 10
m = 5
y = 2021
# print("Today's date is ", d, m, y, sep = '/')
print("Today's date is", end = ' ')
print(d, m, y, sep = '/')
'''
num = int(input())
for i in range(1, 11):
  #print(num, 'X', i, '=', num * i)
  #print(f'{num} x {i} = {num * i}')
  #print('{0} x {1} = {2}'.format(num, i, num * i))
  print('%d x %d = %d'%(num, i, num * i))
