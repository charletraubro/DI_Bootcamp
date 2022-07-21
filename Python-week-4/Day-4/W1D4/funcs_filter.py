even = lambda n: True if n % 2 == 0 else False

numbers = [n for n in range(100)]

print(list(filter(even, numbers)))



restricted = ['Ben','Ron']
accounts = ['Ben','Ron', 'Raz', 'Ran', 'Bill', 'Sam']

allowed = lambda name: True if name not in restricted else False
print(list(filter(allowed, accounts)))