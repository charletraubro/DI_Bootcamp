users = []

user_in = ""

while True:
    user_in = input("Q: Quit; Anything else: continue")

    if user_in == 'Q':
        break

    username, password = input("Username, Password --- ").split(',')

    new_user = {
        'username': username,
        'password': password
    }

    users.append(new_user)


print(users)


