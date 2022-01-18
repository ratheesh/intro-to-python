# Nested for loop
s = 'VIBGYOR'

count = 0
# nested for loop
for i in range(7):
  for j in range(7):
    print(i, j, s[i],s[j])
    count = count + 1
print('The total ways in which the two brothers can wear 7 different colors:', count)