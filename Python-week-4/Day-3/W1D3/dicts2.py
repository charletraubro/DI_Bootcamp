user_a = {
    'first_name': 'Bob',
    'last_name': 'Ross',
    'age': 53,
    'address': 'Tel Aviv',
    'family': [('Jessica', 34), ('Tommy', 8)]
}

print('Tel Aviv' in user_a.values())
print('Tel Aviv' == user_a['address'])
print('first_name' in user_a)


