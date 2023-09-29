number = int(input())
list_of_numbers = []

for each_number in range(number):
    received_number = int(input())
    list_of_numbers.append(received_number)

command = input()
filtered_number = []

if command == 'even':
    for num in list_of_numbers:
        if num % 2 == 0:
            filtered_number.append(num)
elif command == 'odd':
    for num in list_of_numbers:
        if num % 2 != 0:
            filtered_number.append(num)
elif command == 'negative':
    for num in list_of_numbers:
        if num < 0:
            filtered_number.append(num)
else:
    for num in list_of_numbers:
        if num >= 0:
            filtered_number.append(num)

print(filtered_number)