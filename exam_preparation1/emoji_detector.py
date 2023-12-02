import re
list_of_emojies = []
filtered_emojies = []
string = input()
pattern = r"((:{2})([A-Z][a-z]{2,})(:{2})|((\*{2}([A-Z][a-z]{2,})(\*{2}))))"
matches = re.findall(pattern, string)

for match in matches:
    list_of_emojies.append(match[0])

for item in range(len(list_of_emojies)):
    current_string = list_of_emojies[item]
    cutted_string = current_string[2:-2]
    filtered_emojies.append(cutted_string)

coolThresholdSum =
print(f"Cool threshold: {coolThresholdSum}")
