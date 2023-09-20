command = input()
number_of_coffee_needed = 0
while command != "END":
    if command.lower() == 'coding' or command.lower() == 'dog' or \
            command.lower() == 'cat' \
            or command.lower() == 'movie':
        if command.islower():
            number_of_coffee_needed += 1
        elif command.isupper():
            number_of_coffee_needed += 2
    command = input()
if number_of_coffee_needed > 5:
    print('You need extra sleep')
else:
    print(number_of_coffee_needed)
