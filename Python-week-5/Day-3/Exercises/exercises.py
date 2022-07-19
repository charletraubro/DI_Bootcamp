
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
    
#     def __str__(self):
#         print(f'{self.amount}{self.currency}')

#     def __int__(self):
#         print(f'{self.amount}')
    
#     def __repr__(self):
#         print(f'{self.amount}{self.currency}')
    
#     def __add__(self, other):
#         if self.currency == other.currency:
#             return self.amount + other.amount
#         else:
#             return 'Cannot print that'    
   
#     def __iadd__(self, other):
#      return self.amount + self.amount + other.amount

# c1 = Currency('dollars', 5)
# c1.__str__()
# c2 = Currency('dollars', 10)
# c2.__int__()
# c2.__repr__()
# c3 = Currency('shekels', 1)
# c4 = Currency('shekels', 10)

# print(c1.__add__(c3))
# print(c1.__iadd__(c2))

    
# class Zizi:
#     def user():
#         x = int(input('gimme a number: '))
#         import random
#         a = random.randint(1,100)
#         print(f'the computer number is {a}')
#         if a == x:
#             print('you win')
#         else:
#             print('you lose')
#     user()

# import random
# import string

# class Adamsko:
#     def random(length):
#         randomi = string.

import datetime
today_date = datetime.date.today()
print(today_date)