VALID_CHOICES = ['Quit', 'Start', 'X', 'O']

while True:
    try:
        user_in = input('Choice: ')
        if user_in not in VALID_CHOICES:
            raise ValueError()
        break
    except ValueError:
        continue