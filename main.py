class User():
  def sign_in(self):
    print('logged in')

  def attack(self):
    print('do nothing')

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    User.attack(self) # if we want to have both parent & child behavior, we can call parent method inside child method
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Claire', 38)
wizard2 = Wizard('Bennet', 35)
archer1 = Archer('Benson', 32)
archer2 = Archer('Dean', 36)

def player_attack(character):
  character.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, wizard2, archer1, archer2]:
  char.attack()
