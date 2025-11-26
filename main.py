# iterable - list, dictionary, tuple, set, string
# iterated -> one by one check each item in the collection.

for item in (1,2,3,4,5):
  for x in ['a', 'b', 'c']:
    print(item, x)


user = {
  'name': 'Golem',
  'age': 5006,
  'can_swin': False,
}

for item in user:
  print(item)

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for item in user.items():
  key, value = item
  print(key, value)

for key, value in user.items():
  print(key, value)

for item in 50:
  print(item)