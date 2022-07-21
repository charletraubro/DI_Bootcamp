from collections import namedtuple

InfoUser = namedtuple("User", "name date residence")

lista = ['Yossi','Lise','Avner']
listb = [1991,1992,1984]
listc = ['Tel Aviv', 'Ramat Gan', 'Givataim']

members = list(zip(lista, listb, listc))

members_info = []
for name, year, address in members:
    members_info.append(InfoUser(name, year, address))

first_member = members_info[0]

print(first_member)

print(first_member.name)

print(first_member.date)

print(first_member.residence)
