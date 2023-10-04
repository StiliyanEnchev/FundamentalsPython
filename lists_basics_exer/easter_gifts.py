bought_gifts = input().split()
command = input()
while command != "No Money":
    command_and_gift = command.split()
    new_command = command_and_gift[0]
    gift_name = command_and_gift[1]
    if new_command == "OutOfStock":
        for gift in range(len(bought_gifts)):
            if gift_name == bought_gifts[gift]:
                bought_gifts[gift] = None
    elif new_command == "Required":
        index = int(command_and_gift[2])
        if index < (len(bought_gifts)):
            bought_gifts[index] = gift_name
    elif new_command == "JustInCase":
        bought_gifts[-1] = gift_name
    command = input()
for gifts in range(len(bought_gifts)):
    if bought_gifts[gifts] is not None:
        print(bought_gifts[gifts], end=" ")