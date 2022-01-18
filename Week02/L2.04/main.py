# More on variables, operators and expressions

#variable names should beging with alphabet or '_'
#variables beginning with number is not allowed
_a1=20
print(_a1)

print('--------------------')
#variables names are case sensitive
roll=10
rolL=15
ROLL=20
print(roll, rolL, ROLL)

print('---------------')
x,y = 1,2
print(x,y)

print('---------------')
x = y = 2
print(x,y)

# rhs can be both variable or literal
print('---------------')
x,y = 10,20
print(x,y)
x,y = y,x
print(x,y)

print('---------------')
x = 10
print(x)
del(x)
# print(x)

#short hand operators
print('----------------')
count=0
count+=1
count+=1
count+=1
count+=1
print(count)

#short hand operators can be used with all arithmetic operators
print('----------------')
count=10
count-=1
count=count-1
print(count)

print('----------------')
count=10
count*=2
count=count*2
print(count)

print('----------------')
count=10
count/=2
count=count/2
print(count)

# 'in' operator
print('---------------')
print('alpha' in 'A variable can contain alphanumeric characters or underscore chacter')
print('alpha' in 'A variable must start a letters or underscore chacter')


print('----------------')
print('Expresssions')
x=5
print(1< x < 10)
print(10 < x < 20)
print(x < 10 < x*10 < 100)
print(10> x <=9)
print(5==x > 4)
# End of File