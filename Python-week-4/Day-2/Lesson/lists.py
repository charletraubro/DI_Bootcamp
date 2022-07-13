number_list = [1,2,3,4,5]


# Lists - indexing
for i in number_list:
    print(i)

# range(start, end, step)
print(number_list[0::2])
print(number_list[-1::-1])

number_list[2] = 33
print('updated list:', number_list)

numbers_b = [6,7,8,9]

number_list += numbers_b

print('After addition list:', number_list)

number_list *= 2

print('After multiplication list:', number_list)

