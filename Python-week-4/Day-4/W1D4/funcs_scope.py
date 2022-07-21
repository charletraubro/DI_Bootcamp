global_var = 100

def calculation(a, b):
    # local scope
    addition = a + b
    substraction = a - b
    print(global_var)
    return addition, substraction

# global scope
print(calculation(1,2))
print(addition)