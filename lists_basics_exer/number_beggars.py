money_as_strings = input().split(", ")
number_of_beggars = int(input())
money_as_integers = []

for current_money in money_as_strings:
    money_as_integers.append(int(current_money))

list_of_money_for_begger = []
start_index = 0

for beggar in range(number_of_beggars):
    beggars_total_money = 0
    for current_index in range(start_index, len(money_as_integers), number_of_beggars):
        beggars_total_money += money_as_integers[current_index]
    list_of_money_for_begger.append(beggars_total_money)
    start_index += 1
print(list_of_money_for_begger)