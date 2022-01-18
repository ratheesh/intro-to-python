# Find the length of the longest word from the set of words entered by the user

word = input('Enter the word:' )
maxLen = 0

while ( word != '-1'):
  count = 0
  for i in word:
    count = count + 1
  if count > maxLen:
    maxLen = count
  word = input('Enter a word: ')
print(f'Max length word is {maxLen}')
  