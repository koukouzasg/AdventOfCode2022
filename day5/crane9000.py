from collections import deque


def calculate_result(stacks):
    result = ""
    for de in stacks.values():
        result += de.pop()
    return result


def crane9000(movements, stacks):
    for line in movements:
        info = line.split()
        quantity, stackFrom, stackTo = int(info[1]), info[3], info[5]
        deFrom = stacks[stackFrom]
        deTo = stacks[stackTo]
        for i in range(quantity):
            crate = deFrom.pop()
            deTo.append(crate)
    return calculate_result(stacks)


def crane9001(movements, stacks):
    for line in movements:
        info = line.split()
        quantity, stackFrom, stackTo = int(info[1]), info[3], info[5]
        crates = []
        deFrom = stacks[stackFrom]
        deTo = stacks[stackTo]
        for i in range(quantity):
            crates.append(deFrom.pop())
        crates = crates[::-1]
        for crate in crates:
            deTo.append(crate)
    return calculate_result(stacks)


with open("input.txt", "r+") as file:
    lines = file.read().splitlines()

cratesMap = lines[:lines.index("")]
cratesMovements = lines[lines.index("") + 1:]

stacks = {}
stacksInput = cratesMap[-1].replace(" ", "")
cratesMap = cratesMap[:-1]

for c in stacksInput:
    stacks[c] = deque()

for row in cratesMap:
    stackNumber = 1
    for i in range(1, len(row), 4):
        if row[i] != " ":
            de = stacks[str(stackNumber)]
            de.appendleft(row[i])
        stackNumber += 1

# print(crane9000(cratesMovements, stacks))
print(crane9001(cratesMovements, stacks))
