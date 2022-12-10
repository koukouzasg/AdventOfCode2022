def priority(character: str) -> int:
    if character.isupper():
        return abs(ord(character) - 38)
    else:
        return abs(ord(character) - 96)


def get_compartments(rucksack):
    mid = len(rucksack) // 2
    return rucksack[:mid], rucksack[mid:]

prioritySum = 0
with open("input.txt", "r+") as file:
    lines = file.readlines()

lines = [line.rstrip("\n") for line in lines]

for line in lines:
    compartment1, compartment2 = get_compartments(line)
    for char in compartment1:
        if char in compartment2:
            prioritySum += priority(char)
            break
print(prioritySum)

badgeSum = 0
for index in range(0, len(lines)-2, 3):
    rucksack1 = lines[index]
    rucksack2 = lines[index+1]
    rucksack3 = lines[index+2]
    for char in rucksack1:
        if char in rucksack2 and char in rucksack3:
            badgeSum += priority(char)
            print(char)
            break
print(badgeSum)

