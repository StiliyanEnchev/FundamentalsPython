integer = int(input())
for num in range(1, integer + 1):
    current_num = str(num)
    sum_of_digits = 0
    for current_dig in current_num:
        sum_of_digits += int(current_dig)
    if sum_of_digits == 7 or sum_of_digits == 5 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f'{num} -> False')