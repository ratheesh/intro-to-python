# dot product

'''
import random
l = random.sample(list(range(10000)), 1000)

sum = 0
for i in range(len(l)):
  sum += l[i]

print(sum)
'''

# dot product - assume x and y lists are of same length
x = [1,7,3,4]
y = [8,6,3,2]
# dot_product = (1*8) + (7*6) + (3*3) + (4*2)

dot_product = 0
for i in range(len(x)):
  dot_product += (x[i] * y[i])
print(dot_product)