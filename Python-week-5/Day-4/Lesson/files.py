# sentence = 'This is a sentence with/n Two lines of text bla bla.'

# f = open('./sample.txt', mode = 'w')

# f.write(sentence)

# f.close()

# with open('.sample.txt', mode='w') as f:

# sentence = 'This is a sentence with/n Two lines of text bla bla.'
# sentence2 = ['Additional line #1','Additional line #2', 'Additional line #3']

# file_text = ''
# file_text_lines = []
# with open('./sample.txt', mode='r') as f:
#     file_text += f.read()
#     file_text_lines = f.readlines()

# print(file_text)

# with open('./sample.txt', mode='r') as f:
#     f.write(file_text + '/n')
#     f.write(sentence2)
# text = ''
# text_lines = []

# with open('sample.txt', mode = 'r') as f:
#     text += f.read()

# print(text)

import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj)
   #json.dump(obj2save , destination_file)
