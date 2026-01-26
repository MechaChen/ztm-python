class Cat:
    def __init__(self, name, age, color):
        self.color = color
        self.my_dict = {"name": "mi", "age": age}

    def __str__(self):
        return f"Fur color is {self.color}"

    def __len__(self):
        return 13

    def __call__(self):
        return "meow~~"

    def __getitem__(self, index):
        return self.my_dict[index]


scottish_fold = Cat("Scottish Fold", 5, "grey")
print(scottish_fold)
print(str(scottish_fold))
print(scottish_fold.__str__())
print(str("Hello"))
print(scottish_fold())
print(len(scottish_fold))
print(scottish_fold["name"])
