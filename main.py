integers_as_strings = input().split()
remove_count = int(input())
new_integer_list = list(map(int, integers_as_strings))

for num in range(remove_count):
    min_num = min(new_integer_list)
    new_integer_list.remove(min_num)

for index in range(len(integers_as_strings)):
    current_number = int(integers_as_strings[index])
    print(current_number, end=', ')
