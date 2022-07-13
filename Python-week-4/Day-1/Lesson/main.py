# < smaller than
# > bigger than
# <= smaller or equal
# >= bigger or equal
# == equal
# != not equal

# Global scope
from tokenize import Number


username = input('Username: ')
password = input('Password: ')
number = int(input('Number: '))

valid_username = 'yossiA'
valid_password = 'ABC!321'

if (username == valid_username) and (password == valid_password):
    print(f"The password is correct!")

elif number < 5: 
    print(f"Username/Password is Wrong, but the number is correct!")

else:
    print("The username is not valid!")

