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
fill = '$'
empty = ' '
for row in picture:
  for pixel in row:
    if pixel:
      print(fill, end='')
    else:
      print(empty, end='')
  print('\n', end='')
