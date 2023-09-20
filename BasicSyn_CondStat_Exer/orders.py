number_of_orders = int(input())
total_price = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    coffee_price_per_day = days * capsules_per_day * price_per_capsule
    if price_per_capsule < 0.01 or price_per_capsule > 100.00 or days < 1 or days > 31 or capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    total_price += coffee_price_per_day
    print(f"The price for the coffee is: ${coffee_price_per_day:.2f}")
print(f"Total: ${total_price:.2f}")