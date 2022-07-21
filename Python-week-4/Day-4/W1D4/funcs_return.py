def func(name):
    print("Hello "+ name) 
    return "Hello "+ name

welcome = func('Yoosi')
print(welcome)


def func(number):
    num_powered = number ** 2
    return number, num_powered

res = func(2)   

num_orig, num_power = func(2)  

print("original",num_orig)
print("powered",num_power)
