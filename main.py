# OOP
class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')
    return 'done'


player1 = PlayerCharacter('Benson', 32)
player2 = PlayerCharacter('Claire', 38)

print(player1.name)
print(player2.age)

print(player1)
print(player2)

print(player1.run())
print(player1.run)