# Matrix multiplication 1

A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[4,6,8], [2,7,3], [1,9,5]]

C=[[0,0,0], [0,0,0], [0,0,0]]

dim = 3
for i in range(dim):
  for j in range(dim):
    for k in range(dim):
      C[i][j] += A[i][k] * B[k][j]

# C[i][j] = dot product of A[i][...] and B[...][j]
print('Matrix Product: ', C)