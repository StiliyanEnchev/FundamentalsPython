number_of_strings = int(input())
pure = True
for _ in range(number_of_strings):
    strings = input()
    if '.' in strings or '_' in strings or ',' in strings:
        print(f"{strings} is not pure!")
    else:
        print(f"{strings} is pure.")
