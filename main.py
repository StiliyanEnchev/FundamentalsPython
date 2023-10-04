bought_gifts = input().split()
command = input()

while command != "No Money":
    command_and_gift = command.split()
    new_command = command_and_gift[0]
    gift_name = command_and_gift[1]
    if new_command == "OutOfStock":
        for gift in range(len(bought_gifts) - 1, -1, -1):
            if gift_name == bought_gifts[gift]:
                bought_gifts.remove(gift_name)
    elif new_command == "Required":
        given_index = int(command_and_gift[2])
        print(given_index)
        command = input()
