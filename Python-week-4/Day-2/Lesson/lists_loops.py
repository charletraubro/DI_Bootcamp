numbers = [10,20,30,40,50]



# Index looping when looping from the middle
print("Looping through indexes")
for i in range(2, len(numbers), 2):
    print(i)
    print(numbers[i])

# enumerate for looping from the start of the list
print("Looping with enumerate")
for i, val in enumerate(numbers):
    print(i)
    print(val)

print("Looping through items")
for num in numbers[2:]:
    print(num)


product = numbers[0]
for num in numbers[1:]:
    product *= num

print("Product of all numbers:", product)
