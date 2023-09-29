n = int(input())
positive_numbers_list = []
negative_numbers_list = []
for number in range(n):
    new_number = int(input())
    if new_number < 0:
        negative_numbers_list.append(new_number)
    else:
        positive_numbers_list.append(new_number)
print(positive_numbers_list)
print(negative_numbers_list)
print(f'Count of positives: {len(positive_numbers_list)}')
print(f'Sum of negatives: {sum(negative_numbers_list)}')