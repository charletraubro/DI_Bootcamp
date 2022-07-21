lista = ['Yossi','Lise','Avner']
listb = [1991,1992,1984]
listc = ['Tel Aviv', 'Ramat Gan', 'Givataim']

members = list(zip(lista, listb, listc))

# Bonus: named tuples
info_data = []
for user in members:
    user_dict = {
        'name': user[0],
        'year': user[1],
        'residence': user[2]
    }
    info_data.append(user_dict)
print(info_data)

# List comprehension

squared_num = []
for n in range(5,10):
    if n % 2 == 0:
        squared_num.append(n)
        continue
    squared_num.append(n**2)
    
print(squared_num)
# list comprehension
squared_num = [n ** 2 for n in range(5,10)]
print(squared_num)

# dictionary comprehension
dictionary_comp = {key: value for key, value in enumerate('ABC')}
print(dictionary_comp)

