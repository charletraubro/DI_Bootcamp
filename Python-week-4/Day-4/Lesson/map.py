numbers = [1,2,3,4,6,5]

# for i, n in enumerate(numbers):
#     numbers[i] = n ** 2

to_power = lambda n, power: n ** power

def set_power(power):
    return lambda n: n ** power

p2_lambda = set_power(4)

res_list = list(map(lambda n: n ** 2, numbers))

res_list = list(map(p2_lambda, numbers))

print(res_list)