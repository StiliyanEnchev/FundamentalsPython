my_list = []

for _ in range(3):
    string = input()
    my_list.append(string)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)