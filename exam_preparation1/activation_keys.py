activation_key = input()
command = input().split('>>>')

while command[0] != 'Generate':

    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command[0] == 'Flip':
        upper_or_lower, start_index, end_index = command[1], int(command[2]), int(command[3])
        if upper_or_lower == 'Lower':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]
        elif upper_or_lower == 'Upper':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
        print(activation_key)

    elif command[0] == 'Slice':
        start_i, end_i = int(command[1]), int(command[2])
        activation_key = activation_key[:start_i] + activation_key[end_i:]
        print(activation_key)
    command = input().split('>>>')

print(f"Your activation key is: {activation_key}")