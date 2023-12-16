command = input().split(': ')
animal_details = {}
areas_hungry_animal = {}

while command[0] != 'EndDay':
    if command[0] == 'Add':
        animal_name, needed_food_quantity, area = command[1].split('-')
        if animal_name not in animal_details:
            animal_details[animal_name] = [int(needed_food_quantity), area]
        else:
            animal_details[animal_name][0] += int(needed_food_quantity)

    elif command[0] == 'Feed':
        animal_name, food = command[1].split('-')
        if animal_name in animal_details:
            animal_details[animal_name][0] -= int(food)
            if animal_details[animal_name][0] <= 0:
                animal_details.pop(animal_name)
                print(f'{animal_name} was successfully fed')

    command = input().split(': ')

for value in animal_details.values():
    area = value[1]
    if area not in areas_hungry_animal:
        areas_hungry_animal[area] = 0
    areas_hungry_animal[area] += 1

print('Animals:')
for animal, details in animal_details.items():
    print(f" {animal} -> {details[0]}g")
print("Areas with hungry animals:")
for area in areas_hungry_animal:
    print(f"{area}: {areas_hungry_animal[area]}")