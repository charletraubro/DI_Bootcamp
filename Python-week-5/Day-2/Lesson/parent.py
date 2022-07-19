from collections import namedtuple
from time import sleep
import pprint
​
​
Traits = namedtuple("Traits", 'strength intelligence dexterity  defence')
pp = pprint.PrettyPrinter(indent=4)
​
class CharacterTraits:
​
    def __init__(self, strength:int, intelligence:int, dexterity:int, defence:str):
        self.level = 1
        self.xp = 0 
        self.xp_next_level = 100
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.defence = defence
​
    def level_up(self):
        self.level += 1
    
    def set_next_levelXP(self):
        self.xp_next_level += self.level * self.xp_next_level
​
    
​
​
class RPG_CHARACTER:
    """Class for creating RPG character"""
    characters_created = 0
    characters = {}
    def __init__(self, name:str, traits = Traits(0,0,0,0)) -> object:
        self.name = name
        self.traits = CharacterTraits(*traits)
​
        RPG_CHARACTER.characters_created += 1
        RPG_CHARACTER.characters[self.name] = self
​
    def move(self) -> None:
        print(self.name + ' moves')
​
    def strike(self) -> None:
        print(self.name + ' Is striking')
        self.traits.xp += 5
        self.checkXP()
            
    def defence(self) -> None:
        print(self.name + ' Is defending')
        self.traits.xp += 2
        self.checkXP()
​
    def print_characters():     
        pp.pprint(RPG_CHARACTER.characters)
​
    def checkXP(self):
            if self.traits.xp >= self.traits.xp_next_level:
                self.traits.level_up()
                self.traits.set_next_levelXP()
                print(f"{self.name} is Leveled UP! Now level is {self.traits.level}")
            else:
                pass