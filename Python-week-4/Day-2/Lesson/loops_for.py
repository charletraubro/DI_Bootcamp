# for num in range(10,100,10):
#     print(num)

# 2
for num_a in range(1,11):
    #num_a = 2

    mult_table_num = ""

    for num_b in range(1, 11):
        # num_b = 1 
        mult_table_num += f'{num_a * num_b}|'
        #mult_table_num = '2|4|6|8|...20|'
    # print(mult_table_num)


a_str = 'ABCDE'

# for char in a_str:
#     print(char)

a_list = [1,2,'a','TExt', [1,{1,2,3,4,5}]]

for item in a_list:
    print(item)

# print(a_list[-1][1])

# for idx, item in enumerate(a_list[:3]):
#     print(idx, item)




# Range - loop through numbers and loop at the middle of a sequence
for num in range(0,10,1):
    print(num)

names = ['Yossi', 'Lise', 'Rashad','Roi','Roy']
for name_idx in range(2, len(names)):
    print(names[name_idx])


# enumerate(Sequence)
for idx, name in enumerate(names):
    if idx == 2:
        print("Breaking the loop")
        break
    print(idx,name)

# Looping through items in Sequence
for name in names:
    print(name)