# Dictionary Keys
dictionary = {
  123: [1, 2, 3],
  True: 'hello',
  '[100]': True,
}

another_dictionary = {
  '123': [1, 2, 3],
  '123': 'hello',
}

print(dictionary['[100]'])
print(another_dictionary['123'])