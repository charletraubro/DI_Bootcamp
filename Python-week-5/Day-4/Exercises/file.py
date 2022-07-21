# text_string = ''
# text_lines = []



# with open('/Users/charlestraubro/Desktop/Coding-2022/Python-week-5/Day-4/Exercises/text.txt', mode = 'r') as f:
#     text_string += f.read()
#     f.seek(0)
#     text_lines = f.readlines()

# print(text_string)



# with open('/Users/charlestraubro/Desktop/Coding-2022/Python-week-5/Day-4/Exercises/text.txt') as f:
#     lines = f.readlines()

# print(type(lines))
# print(lines)

# import random

# words_list = []

# def get_words_from_file():
#     f = open('/Users/charlestraubro/Desktop/Coding-2022/Python-week-5/Day-4/Exercises/text.txt')
#     data = f.readlines()
#     for i in range(len(data)):
#         words_list.append(data[i].strip('\n'))
#     return words_list

# print(get_words_from_file())

# def get_random_sentence(length):
#     length = int(input("give me a number between 2 and 20: "))
#     if (length < 2):
#         print("error") 
#     elif (length > 20):
#         print("error")
#     else:
#         for i in range(length):
#             print(random.choice(words_list).lower(), end = ' ')
# get_random_sentence(6)

# for i in range(9):
#     length = random.choice(get_words_from_list('/Users/charlestraubro/Desktop/Coding-2022/Python-week-5/Day-4/Exercises/text.txt'))


# print(length)

#ex2
# import json 

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# data = json.loads(sampleJson)
# a = data['company']['employee']['payable']['salary']
# print(a)

# data['company']['employee']['birth_date'] = '09/06/2003'
# print(data)

# with open('sampleJson.json', 'w') as f:
#     json.dump(data, f, indent = 2, sort_keys=True)