companions_count = int(input())
days_of_adventure = int(input())
total_coins = 0
for day in range(1, days_of_adventure + 1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
    total_coins += 50 - (companions_count * 2)
    if day % 3 == 0:
        total_coins -= companions_count * 3
    if day % 5 == 0:
        total_coins += companions_count * 20
        if day % 3 == 0:
            total_coins -= companions_count * 2
coins_per_companion = total_coins // companions_count
print(f"{companions_count} companions received {coins_per_companion} coins each.")