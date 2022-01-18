
hor_line='ABCDEFGH'

start = input()
end = input()

hor_move = hor_line.index(start[0]) - hor_line.index(end[0])
hor_move = int((hor_move * hor_move) ** 0.5)

vert_move = int(start[1]) - int(end[1])
vert_move = int((vert_move * vert_move) ** 0.5)

# print('hor_move', hor_move)
# print('vert_move', vert_move)

if (hor_move == vert_move):
  print('YES')
else:
  print('NO')
