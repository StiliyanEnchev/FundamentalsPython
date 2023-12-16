import re

number = int(input())
pattern = r'^(\$|%)([A-Z][a-z]{2,})(\1)(: )\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

for _ in range(number):
    message = input()
    matches = re.findall(pattern, message)

    if not matches:
        print('Valid message not found!')
    else:
        for item in matches:
            tag = item[1]
            dectipted_message = chr(int(item[4])) + chr(int(item[5])) + chr(int(item[6]))
        print(f"{tag}: {dectipted_message}")