
endSeq='abcdefghijklmnopqrstuvwxyz'
shortStr = 'fsdfdslfdskfldfkdfjdkfdfsfdsfdfdsfdsfdsfsdfsdfkdsjfldskfjalksdfjsdfldkfjdsfdfdf'
while True:
  str = input()
  if (str == endSeq):
    print(shortStr)
    break
  else:
    if (len(str) < len(shortStr)):
      shortStr = str
