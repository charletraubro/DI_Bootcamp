a_set = {1,2,3,4}

a_set = set({})

print(type(a_set))

# For removing duplicates
duplicates_list = [1,1,1,2,2,'a','c']

list_to_set = set(duplicates_list)

liost_without_duplicates = list(list_to_set)

print(list_to_set)

colors_a = {'red','green','blue','pink'}
colors_b = {'grey','green','blue','yellow'}

# & - intersection
print("Intersection:", colors_a & colors_b)
# | - union
print("Union:", colors_a | colors_b)
# | - Without interection
print("Without interection:", colors_a ^ colors_b)
# - (minus) - difference
print("Difference a - b:",colors_a - colors_b)
print("Difference b - a:",colors_b - colors_a)


