number_of_snowballs = int(input())
highest_weight = 0
highest_time = 0
highest_quality = 0
highest_snowball = 0
for num in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_snowball = int((weight / time_needed) ** quality)
    if highest_snowball < current_snowball:
        highest_snowball = current_snowball
        highest_quality = quality
        highest_time = time_needed
        highest_weight = weight
print(f"{highest_weight} : {highest_time} = {highest_snowball} ({highest_quality})")