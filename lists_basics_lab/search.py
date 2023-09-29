num = int(input())
word = input()
list_of_words = []
filtered_list_of_words = []
for lines in range(num):
    strings = input()
    list_of_words.append(strings)

for current_string in list_of_words:
    if word in current_string:
        filtered_list_of_words.append(current_string)

print(list_of_words)
print(filtered_list_of_words)