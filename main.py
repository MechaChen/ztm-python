user = {
  'basket': [1, 2, 3],
  'greet': 'hello',
  'age': 20,
}

print('basket' in user)
print('hello' in user.keys())
print('hello' in user.values())
print(user.items())

print(user.pop('age'))
print(user)

user.update({ 'greet': 'hi' })
print(user)

user2 = user.copy()

user.clear() # remove all items from the dictionary
print(user)

print(user2)