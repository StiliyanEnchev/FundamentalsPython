number = int(input())
all_pieces = {}

for num in range(number):
    piece, composer, key = input().split("|")
    all_pieces[piece] = [composer, key]

command = input().split('|')

while command[0] != "Stop":

    if command[0] == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece in all_pieces.keys():
            print(f"{piece} is already in the collection!")
            command = input().split('|')
            continue
        all_pieces[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")

    elif command[0] == 'Remove':
        piece = command[1]
        if piece in all_pieces.keys():
            all_pieces.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif command[0] == 'ChangeKey':
        piece, new_key = command[1], command[2]
        if piece in all_pieces.keys():
            all_pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input().split('|')

for piece in all_pieces:
    composer, key = all_pieces[piece][0], all_pieces[piece][1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")