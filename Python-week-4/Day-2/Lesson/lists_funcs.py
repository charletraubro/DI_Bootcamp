a = []

# adding items - append to add to end of list
a.append(1)
print(a)

# insert
a.insert(0, 0)
print(a)

a.append(1)
print(a)

# To remove first occurance of 1
a.remove(1)
print(a)

# To remove first index value
del a[0]
print(a)

a += [2,3,4]
a.pop()
print(a)

eligible_users = ['Yossi','David','Reuven']

# Pop for removing by index + returning 
blocked_user = eligible_users.pop(0)
print(blocked_user)

# Sorting items
char_list = ['z','b','f','a','d']

# sorted(list) to sort and return new (sorted) list
sorted_char_list = sorted(char_list)

print(sorted_char_list)

# .sort() to sort inplace
char_list.sort()

print("Original list after sort():",char_list)

