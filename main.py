# class method & static method
class PlayerCharacter:
  def __init__(self, name = 'anonymous', age = 0):
    if age > 18:
      self.name = name
      self.age = age

  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Teddy', num1 + num2)

  @staticmethod
  def adding_things2(num1, num2):
    return num1 + num2

player1 = PlayerCharacter.adding_things(13,14)
print(player1.name, player1.age)
print(PlayerCharacter.adding_things2(5,6))