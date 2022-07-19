zina = RPG_CHARACTER("Zina", traits = (100, 150, 120, 'Warrior', 300))

def main():
    choices = ['strike', 'defence', 'move']    
    conan = RPG_CHARACTER("Conan", traits = (100, 150, 120, 'Warrior', 300))

    while conan.traits.level < 3:
        action = random.choice(choices)
        if action == 'strike':
            conan.strike()
        if action == 'defence':
            conan.defence()
        if action == 'move':
            conan.move()
        sleep(0.1)

main()