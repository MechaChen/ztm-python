# Dictionary Methods
user = {
  'basket': [1, 2, 3],
  'greet': 'hello',
}

# print(user['age']) # will throw KeyError
print(user.get('age')) # will just return None, not throw KeyError
print(user.get('age', 55)) # will return 55 if 'age' is not in the dictionary

# not the common way to create a dictionary
user2 = dict(name='Benson')
print(user2)