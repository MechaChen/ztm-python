# OOP
class PlayerCharacter:
  membership = True # class object attribute: belongs to the class, not the instance

  def __init__(self, name, age):
    if PlayerCharacter.membership: # can be accessed by the class or the instance
      self.name = name
      self.age = age

  def shout(self):
    print(f'my name is {self.name}')

  def run(self):
    print('run')
    return 'done'


player1 = PlayerCharacter('Benson', 32)
player2 = PlayerCharacter('Claire', 38)

print(player1.name)
print(player2.age)

print(player1)
print(player2)

print(player1.shout())
print(player1.run)