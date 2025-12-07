# Exercise!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# do not hint me
for row in picture:
  for pixel in row:
    if pixel == 1:
      print('*', end='')
    else:
      print(' ', end='')
  print('\n', end='')
