a_tuple = (1,2,3)

print(a_tuple)

a_tuple = 1,2,3

print(a_tuple)

person_1 = ('Yossi', 'Yossi@gmail.com', 30)
person_2 = ('Ayala', 'Ayala@gmail.com', 25)

# person_1[0] = 'Raz'

a = 5
b = 10

a, b = b, a
print(a)
print(b)


name = person_1[0]
print(name)

# map(function, sequence(list, tuple, dictionary, str))
# num1, num2, num3 = map(int ,input("Gimme numbers").split(','))
# ['1','2','3']
# int('1')
# int('2')
# int('3')
# print('num1:',num1 * 10)
# print('num2:',num2)
# print('num3:',num3)


a_tuple = (10, 20, 30, 40)

a, b, c, d = a_tuple

print(a)
print(b)
print(c)
print(d)