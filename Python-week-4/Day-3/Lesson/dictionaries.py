# Creating dictionary
user_a = {
    'first_name': 'Bob',
    'last_name': 'Ross',
    'age': 53,
    'address': 'Tel Aviv',
    'family': [('Jessica', 34), ('Tommy', 8)]
}

# Accessing dictionaries values
print(user_a['first_name'].upper())
print(user_a['family'][1])


# Looping through dictionary keys
for key in user_a.keys():
    print("Key:",key)

# Looping through dictionary values
for value in user_a.values():
    print("Value:",value)

# Looping through dictionary keys and values
for key, value in user_a.items():
    print("K and V:", (key,value))

# Popping values by key
name_removed = user_a.pop('first_name')

print(user_a)
print("Name removed:",name_removed)

# Deleting (without removal) values by key
del user_a['last_name']
# print(user_a)

user_a['first_name'] = name_removed

# print(user_a)

user_a['first_name'] = 'BOBBY'
print(user_a)


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])

