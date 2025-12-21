# parameters: the variables defined in the function definition
# default parameters: the parameters with default values
def say_hello(name='No Body', emoji='👻'):
  print(f'hello {name}, {emoji}')

# positional arguments: the actual values passed to the function
say_hello('Benson', '🥇')
say_hello('Mark', '🥈')
say_hello('Dean', '🥉')
say_hello('Robot')

# keyword arguments: the arguments passed to the function by name
say_hello(emoji='🥇', name='Benson')