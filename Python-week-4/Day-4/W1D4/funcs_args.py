# *args = arguments 

def print_names(*names: tuple) -> None: 
    for name in names:
        print(name)

print_names('yossi','david','raz','shlomo','whatever')

def return_args(*args) -> list:
    args_list = []
    for arg in args:
        if isinstance(arg, str):
            args_list.append(arg * 2)
        elif isinstance(arg, int):
            args_list.append(arg ** 2)
        else:
            args_list.append(arg)
    return args_list

result = return_args(1,2,3,'ABC','BVC',[123])

print(result)