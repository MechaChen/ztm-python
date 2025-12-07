def say_hello():
  print('hello')

say_hello()

def show_tree():
  tree = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
  ]

  for row in tree:
    for pixel in row:
      if pixel:
        print('*', end='')
      else:
        print(' ', end='')
    print('')

print(show_tree)
show_tree()