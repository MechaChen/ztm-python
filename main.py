# formatted strings

name = 'Benson'
age = 32

print(f'Hi {name}. You are {age} years old.')

print('Hi {}. You are {} years old.'.format(name, age))

print('Hi {1}. You are {0} years old.'.format(name, age))

print('Hi {new_name}. You are {age} years old.'.format(
  new_name="Benson Chen", age=31
))