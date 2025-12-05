# enumerate() will give us the index and the enumerated object
from re import S


for i, char in enumerate('Helllooo'):
  print(i, char)

print('--------------------------------')

for i, char in enumerate(('a', 'b', 'c')):
  print(i, char)

print('--------------------------------')

for i, char in enumerate(range(100)):
  if char == 50:
    print(f'index of 50 is: {i}')