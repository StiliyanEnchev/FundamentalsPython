lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_breaks = 0
expenses = 0
for loss in range(1, lost_fights_count + 1):
    if loss % 2 == 0:
        expenses += helmet_price
    if loss % 3 == 0:
        expenses += sword_price
        if loss % 2 == 0:
            expenses += shield_price
            shield_breaks += 1
            if shield_breaks % 2 == 0:
                expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")