password = input()
command = input().split()

while command[0] != 'Done':
    if command[0] == 'TakeOdd':
        new_pass = ''
        for index in range(len(password)):
            if index % 2 != 0:
                new_pass += password[index]
        password = new_pass
        print(password)

    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        password = password[:index] + password[index+length:]
        print(password)

    elif command[0] == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring not in password:
            print("Nothing to replace!")
        else:
            while substring in password:
                password = password.replace(substring, substitute)
                print(password)


    command = input().split()

print(f'Your password is: {password}')
