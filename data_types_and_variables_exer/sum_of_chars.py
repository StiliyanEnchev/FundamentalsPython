number_of_letters = int(input())
total_sum = 0
for num in range(number_of_letters):
    letter = input()
    total_sum += ord(letter)
print(f'The sum equals: {total_sum}')