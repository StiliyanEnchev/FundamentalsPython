all_fire_cells = input().split('#')
left_water = int(input())
effort_counter = 0
total_water = left_water

for cell_number in range(len(all_fire_cells)):
    current_cell_fire_details = (all_fire_cells[cell_number]).split(" = ")
    fire_type, fire_volume = current_cell_fire_details[0], int(current_cell_fire_details[1])

    if fire_type == 'High':
        if left_water >= fire_volume and 81 <= fire_volume <= 125:
            left_water -= fire_volume
            effort_counter += fire_volume * 0.25
        else:
            all_fire_cells[cell_number] = None
    elif fire_type == 'Medium':
        if left_water >= fire_volume and 51 <= fire_volume <= 80:
            left_water -= fire_volume
            effort_counter += fire_volume * 0.25
        else:
            all_fire_cells[cell_number] = None

    elif fire_type == 'Low':
        if left_water >= fire_volume and 1 <= fire_volume <= 50:
            left_water -= fire_volume
            effort_counter += fire_volume * 0.25
        else:
            all_fire_cells[cell_number] = None

total_putted_fire = total_water - left_water

print(f'Cells:')
print(f'Effort: {effort_counter:.2f}')
print(f'Total Fire: {total_putted_fire}')