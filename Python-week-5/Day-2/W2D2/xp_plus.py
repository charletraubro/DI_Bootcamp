from typing import List, Dict

class Family:

    def __init__(self, last_name:str, members:List[Dict]) -> object:
        self.last_name = last_name
        self.members = members

    def born(self, child) -> None:
        self.members.append(child)
        print("Congrats for the new baby!")

    def get_member(self, name):
        for member in self.members:
            if name == member['name']:
                return member
        else:
            raise ValueError(f"No such member with name {name}")


    def is_18(self, name):
        member = self.get_member(name)
        if member['age'] >= 18:
            return True
        else:
            return False
        

    def family_presentation(self):
        members_print = ''

        for member in self.members:
            members_print += f'''Name: {member['name']}, Age: {member['age']}\n'''
        
        output = f""" The {self.last_name} Family
        ------------------\n{members_print}
        """
        print(output)


data = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

# straussFamily = Family('Strauss', data)
# new_child = {'name':'Tommy','age':0,'gender':'Male','is_child':True}
# straussFamily.born(new_child)
# straussFamily.family_presentation()


class TheIncredibles(Family):
    
    def use_power(self, name:str) -> None:
        member = self.get_member(name)
        if self.is_18(name):
            print(f"{member['name']} is using power: {member['power']}!")
        else:
            raise ValueError('Member is under 18!')
            
    def family_presentation(self):
        super().family_presentation() # Original part
        power_stack = '|'.join([member['power'] for member in self.members])
        print(f'Power Stack: {power_stack}')            



data2 = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]


incredible_fam = TheIncredibles('Incredible', data2)

incredible_fam.use_power('Sarah')

incredible_fam.family_presentation()