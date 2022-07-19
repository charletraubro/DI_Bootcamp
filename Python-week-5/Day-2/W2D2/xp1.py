class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

    def sing(self, sounds):
        return f'{sounds}'

class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass

class Siamese(Cat):
    pass

bengal = Bengal('Bob', 1)
chartreux = Chartreux('George', 2)
siamese = Siamese('Sonia', 5)

all_cats = [bengal, chartreux, siamese]
bengal.walk()

saras_pets = Pets(all_cats)

saras_pets.walk()