
# -5 ---- -4.5 ---- -4 ....-1--0-- +1,....
real = float(input())
integer  = int(real)

if ( real == integer):
  min_int = integer
else:
  if (real < 0):
    integer -= 1
  min_int = integer + 1

max_int = integer

print(max_int)
print(min_int)
