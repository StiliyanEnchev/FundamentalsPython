spell = input()
command = input().split()

while command[0] != 'Abracadabra':

    if command[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)

    elif command[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)

    elif command[0] == 'Illusion':
        index, letter = int(command[1]), command[2]
        if len(spell)-1 >= index:
            spell = spell[:index] + letter + spell[index+1:]
            print('Done!')
        else:
            print('The spell was too weak.')

    elif command[0] == 'Divination':
        first_substr, second_substr = command[1], command[2]
        if first_substr in spell:
            spell = spell.replace(first_substr, second_substr)
            print(spell)

    elif command[0] == 'Alteration':
        substr = command[1]
        if substr in spell:
            spell = spell.replace(substr, '')
            print(spell)
    else:
        print('The spell did not work!')

    command = input().split()
