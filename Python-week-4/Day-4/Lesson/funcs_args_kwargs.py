# {
#     'Yossi': {
#         'Address': '',
#         'Zip': -1,
#         'Phone': -1
#     },
#     'Lise': {
#         'Address': '',
#         'Zip': -1,
#         'Phone': -1
#     },
#     'Reuven': {
#         'Address': '',
#         'Zip': -1,
#         'Phone': -1
#     }
# }
def make_details(*names: tuple, **details: dict) -> dict:
    full_details = {}
    for name in names:
        full_details[name] = details
    return full_details

f_details = make_details('Yossi','Lise','Reuven', Address = '', Zip = -1, Phone = -1)

print(f_details)