total_budget = float(input())
price_per_1kg_flour = float(input())
price_for_1pack_of_eggs = price_per_1kg_flour * 0.75
price_for_1l_milk = price_per_1kg_flour * 1.25
price_per_250_milk = price_for_1l_milk * 0.25
price_per_one_loav = price_per_250_milk + price_per_1kg_flour + price_for_1pack_of_eggs
number_of_loaves = 0
colored_eggs = 0

while total_budget > price_per_one_loav:
    total_budget -= price_per_one_loav
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {total_budget:.2f}BGN left.")