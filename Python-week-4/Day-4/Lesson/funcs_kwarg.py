# kwargs = key value argument

from unicodedata import name


def some_func(a, b):
    print(a, b)

some_func(5, b=5)

# some_func(a=5, 5)

def create_dict_func(**details) -> dict:
    return details

details_yossi = create_dict_func(name = 'Yossi', address = 'Tel Aviv', country = 'Israel', children = ['Bob','Ross'])
details_lise = create_dict_func(name = 'Lise', address = 'Holon', country = 'Israel', gender = 'F')

print(details_yossi)
print(details_lise)
