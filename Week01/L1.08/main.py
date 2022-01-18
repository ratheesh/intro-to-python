# Data Types 2
i = 10
f = 1.6
s = 'hello'
b1 = True
b2 = False

print(type(i))
print(type(f))
print(type(s))
print(type(b1))
print(type(b2))
print('--------------')
# =============

a = int(5.7)
b = int('10')
# c = int('8.3') -> Error
print(a, type(a))
print(b, type(b))
# print(c, type(c))

print('--------------')
a = float(9)
b = float('6.3')
print(a, type(a))
print(b, type(b))

print('---------------')
a = str(9)
b = str(5.3)
print(a, type(a))
print(b, type(b))

print('---------------')
a = bool(10)
b = bool(0)
c = bool(-10)
print(a, type(a))
print(b, type(b))
print(c, type(c))

print('---------------')
a = bool(10.0)
b = bool(0.0)
c = bool(-10.5)
print(a, type(a))
print(b, type(b))
print(c, type(c))

print('---------------')
b = bool('India')
a = bool('10')
c = bool('-10.5')
d = bool('0')
e = bool('')
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))