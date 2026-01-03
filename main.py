class PlayerCharacter:
  def __init__(self, name, age):
    if age > 18:
      self.name = name
      self.age = age

  def speak(self):
    print(f'my name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter('Benson', 32)
player1.speak()