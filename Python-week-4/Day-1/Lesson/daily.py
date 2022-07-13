import random

user_string = input('Gimme a string: ')

if len(user_string) < 10: 
    print("string is small")

elif len(user_string) > 10:
    print("string is big")

else:
    print("string is 10 characters long")

print("First character:", user_string[0])
print("Last character:", user_string[-1])

output_string = ''
for character in user_string:
    output_string += character
    print(output_string)


shuffled = "".join(random.sample(user_string, len(user_string)))
print("Shuffled:", shuffled)