integers_as_strings = input().split()
remove_count = int(input())
new_integer_list = []

for index in range(len(integers_as_strings)):
    current_number = int(integers_as_strings[index])
    new_integer_list.append(current_number)

for num in range(remove_count):
    min_num = min(new_integer_list)
    new_integer_list.remove(min_num)

formatted_list = ', '.join(map(str, new_integer_list))
print(formatted_list)