class User:
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, email, age, power):
        super().__init__(name, email, age)
        self.power = power

    def attack(self):
        User.attack(
            self
        )  # if we want to have both parent & child behavior, we can call parent method inside child method
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, age, email, num_arrows):
        self.name = name
        self.age = age
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows}")


wizard1 = Wizard("Claire", "chillymood@gmail.com", 38, 100)
archer1 = Archer("Benson", "tumlivein@gmail.com", 32, 10)

print(dir(wizard1))
print(dir(archer1))
