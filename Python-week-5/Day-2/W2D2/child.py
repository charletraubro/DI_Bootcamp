from time import sleep
from parent import CharacterTraits
from parent import RPG_CHARACTER
import pprint
pp = pprint.PrettyPrinter(indent=4)


class Warrior(RPG_CHARACTER):
    
    def __init__(self, name: str, traits=...) -> object:
        super().__init__(name, traits)
        self.traits = CharacterTraits(*traits, physical_power = 10)
        self.character_class = 'Warrior'
        self.physical_power = 10

    def sprint(self):
        self.traits.xp += 2
        print(f"{self.name} now is Sprinting!")
        self.checkXP()
    

class Mage(RPG_CHARACTER):

    def __init__(self, name: str, traits=...) -> object:
        super().__init__(name, traits)
        self.character_class = 'Mage'
        self.magic_power = 10

    def cast_spell(self):
        self.traits.xp += 2
        print(f"{self.name} now is Casting Spell!")
        self.checkXP()
        

conan = Warrior("Conan", traits = (100, 150, 120, 300))
print(type(conan))

gendalf = Mage("Gendhalf", traits = (50, 100, 145, 250))

pp.pprint(conan.__dict__)
pp.pprint(gendalf.__dict__)

conan.sprint()
gendalf.cast_spell()

print(conan.traits)