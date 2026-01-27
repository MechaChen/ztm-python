class User:
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left - {self.num_arrows}")

    def check_arrows(self):
        print(f"Arrows left: {self.num_arrows}")

    def run(self):
        print("ran really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


hb1 = HybridBorg("Benson", 50, 100)
hb1.sign_in()
hb1.attack()  # 1st inherit will dominate the method, so it will use Wizard's attack method
hb1.check_arrows()
hb1.run()
