class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class BritishShorthair(Cat):
    def sing(self, sounds):
        return f"{sounds}"

    def walk(self):
        return f"{self.name} is walking with meowing"


class ScottishFold(Cat):
    def sing(self, sounds):
        return f"{sounds}"

    def walk(self):
        return f"{self.name} is walking cutely"


# 1 Add nother Cat
class Ragdoll(Cat):
    def sing(self, sounds):
        return f"{sounds}"

    def walk(self):
        return f"{self.name} is walking gracefully"


# 2 Create a list of all of the pets (create 3 cat instances from the above)
british_shorthair = BritishShorthair("British Shorthair", 3)
scottish_fold = ScottishFold("Scottish Fold", 2)
ragdoll = Ragdoll("Ragdoll", 4)
my_cats = [british_shorthair, scottish_fold, ragdoll]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
