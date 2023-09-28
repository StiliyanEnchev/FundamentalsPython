liters_of_the_tank = 255
number_of_lines = int(input())
liters_in_tank = 0
for line in range(number_of_lines):
    filling_litters = int(input())
    if liters_of_the_tank < filling_litters:
        print('Insufficient capacity!')
    else:
        liters_of_the_tank -= filling_litters
        liters_in_tank += filling_litters
print(liters_in_tank)