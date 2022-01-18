# More on strings

# replication
s='good'
print(s * 5)
print(s[0] * 5)

print('----------------')
# comparison
x = 'India'
print(x == 'India')
print(x == 'india')

print('----------------')
print('apple' > 'one')
print('four' < 'ten')

print('----------------')
print('ab' < 'az')
print('abcedef' < 'abcde')

print('----------------')
# indexing
s='python'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

print('negative indexing')
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])

print('-----------------')
# length of string -> dealing with out of range errors
s='asdfjlkqwertyuiop'
print('len of string:', len(s))
