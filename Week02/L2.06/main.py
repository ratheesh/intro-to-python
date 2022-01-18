# String Methods
print('Basic string methods\n')

x='pytHoN sTrIng mEthOdS'
print('Input:', x)
print('lower():', x.lower())
print('upper():', x.upper())
print('capitalize():', x.capitalize())
print('title():', x.title())
print('swapcase():', x.swapcase())

print('------------------')
print('Boolen output methods')
x = 'Python Module'
print('Input:', x)
print('islower():', x.islower())
print('isupper():', x.isupper())
print('istitle():', x.istitle())

print('--------------------')
print('alphanumeric test')
x='abc'
print('Input:', x)
print('isdigit():', x.isdigit())
print('isalpha():', x.isalpha())
print('isalnum():', x.isalnum())

print('--------------------')
print('Trimming functions')
x='      Python      '
print('Input:', x)
print('strip():', x.strip())
print('rstrip():', x.rstrip())
print('lstrip():', x.lstrip())
#Note: Only empty lines and other esc characters are trimmed

print('--------------------')
print('starting/ending functions')
x='Python'
print('Input:', x)
print('startswith("P"):', x.startswith('P'))
print('endswith("n"):', x.endswith('n'))
print('endswith("o"):', x.endswith('o'))

print('--------------------')
print('count/indexing/replace functions')
x='Python String Methods'
print('Input:', x)
print('count("x"):', x.count('n'))
print('index("S"):', x.index('S'))
print('index("s"):', x.index('s'))
print('replace("S","s"):', x.replace('S', 's'))
print('replace("M","m"):', x.replace('M', 'm'))
print('replace("s"," "):', x.replace('s', ' '))
