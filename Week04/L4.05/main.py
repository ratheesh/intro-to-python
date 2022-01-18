# obvious sort

l = [ 12,10,6,32,5,98,13,4,42,5,75]
x=[]

while len(l) != 0:
  min = l[0]
  for i in range(len(l)):
    if l[i] < min:
      min = l[i]
  x.append(min)
  l.remove(min)

print('Sorted List: ', x)