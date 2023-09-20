budget = int(input())
total_spend = 0
while total_spend <= budget:
    spend_price = input()
    if spend_price == "End":
        print("You bought everything needed.")
        break
    total_spend += float(spend_price)
else:
    print("You went in overdraft!")