def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]
    sequences = [(line.split()[0], int(line.split()[1])) for line in lines]

head, tail = (0, 0), (0, 0)
visited = set()
visited.add(tail)

for sequence in sequences:
    for i in range(sequence[1]):
        if sequence[0] == 'L':
            head = (head[0]-1, head[1])
        elif sequence[0] == 'R':
            head = (head[0] + 1, head[1])
        elif sequence[0] == 'U':
            head = (head[0], head[1] + 1)
        else:
            head = (head[0], head[1] - 1)
        xDiff = head[0] - tail[0]
        yDiff = head[1] - tail[1]
        if abs(xDiff) > 1 or abs(yDiff) > 1:
            tail = (tail[0] + sign(xDiff), tail[1] + sign(yDiff))
            visited.add(tail)

print(len(visited))

# Part2
visited = set()
knots = []
for i in range(10):
    knots.append((0, 0))

for sequence in sequences:
    for i in range(sequence[1]):
        if sequence[0] == 'L':
            knots[0] = (knots[0][0]-1, knots[0][1])
        elif sequence[0] == 'R':
            knots[0] = (knots[0][0]+1, knots[0][1])
        elif sequence[0] == 'U':
            knots[0] = (knots[0][0], knots[0][1]+1)
        else:
            knots[0] = (knots[0][0], knots[0][1]-1)
        for k in range(len(knots)-1):
            xDiff = knots[k][0] - knots[k+1][0]
            yDiff = knots[k][1] - knots[k+1][1]
            if abs(xDiff) > 1 or abs(yDiff) > 1:
                knots[k+1] = (knots[k+1][0] + sign(xDiff), knots[k+1][1] + sign(yDiff))
                visited.add(knots[-1])

print(len(visited))
