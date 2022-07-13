from traceback import print_tb


password = input('Password: ')

number_takes = 0

while password != 'ABC':
    print('Looping')
    password = input('Password: ')
    if password == 'ACB':
        print('Breaking')
        break
    if password == 'Continue':
        continue
    number_takes += 1
else:
    print('Correct password provided!')
    print(number_takes)