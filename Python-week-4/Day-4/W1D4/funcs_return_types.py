def calculation(a: int, b: int) -> tuple:
    # local scope
    addition = a + b
    substraction = a - b
    print(global_var)
    return addition, substraction

def welcome_statement(name: str, gender: str) -> str:
    if gender == 'M':
        return f"Hello Mr.{name}"
    if gender == 'F':
        return f"Hello Ms.{name}"

def allowed(accounts: list, restricted: list) -> list:
    allowed_list = []
    for account in accounts:
        if account not in restricted:
            allowed_list.append(account)

    return allowed_list

def allowed(accounts: list, restricted: list) -> list:
    """ method for finding the allowed profiles in a list
    """
    allowed_list = []
    for account in accounts:
        if account not in restricted:
            allowed_list.append(account)

    return allowed_list


# help(allowed)