# import this


def func_name():
    print('Something')


def func_name(print_this):
    print(f"{print_this}")


def func_name(print_this = 'Hello'):
    print(f"{print_this}")
    
func_name()
func_name('Else')
