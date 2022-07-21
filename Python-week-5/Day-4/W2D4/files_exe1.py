text_string = ''
text_lines = []

with open('/Users/charlestraubro/Desktop/Coding-2022/Python-week-5/Day-4/W2D4/star_wars.txt', mode = 'r') as f:
    text_string += f.read()
    f.seek(0)
    text_lines = f.readlines()

# 1
# for line in enumerate(text_lines):
#     print(line)

# 2
print(text_string[:5])

# 3
print(text_lines[4])

# 4.1
# stript_new_line = lambda s: s.strip('\n')
# text_lines = list(map(stript_new_line, text_lines))
# names_uniques = list(set(text_lines))

# count_names = {name: 0 for name in names_uniques}

# for name in text_lines:
#     count_names[name] += 1

# print(count_names)

# # 4.2
# from collections import Counter

# count_names = Counter(text_lines)

# # 5 
# with open('./star_wars.txt', mode = 'a') as f:
#     f.write('\nYossi')

# # 6
# for i, name in enumerate(text_lines):
#     if name == 'Luke':
#         text_lines[i] += ' Skywalker'

# with open('./star_wars.txt', mode = 'w') as f:
#     for line in text_lines:
#         f.write(line + '\n')

