def create_grid() -> [[int]]:
    with open("input.txt") as file:
        lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]
    grid = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for x, row in enumerate(lines):
        for y, z in enumerate(row):
            grid[x][y] = int(z)
    return grid


def scan_horizontally(treeGrid, treePos):
    x, y = treePos[0], treePos[1]
    left, right = False, False
    tree = treeGrid[x][y]
    for r in range(len(treeGrid)):
        if r == y:
            continue
        if treeGrid[x][r] >= tree:
            if r < y:
                left = True
            else:
                right = True
        if left and right:
            return True
    return False


def scan_vertically(treeGrid, treePos):
    x, y = treePos[0], treePos[1]
    upper, lower = False, False
    tree = treeGrid[x][y]
    for r in range(len(treeGrid)):
        if r == x:
            continue
        if treeGrid[r][y] >= tree:
            if r < x:
                upper = True
            else:
                lower = True
        if upper and lower:
            return True
    return False


def calculate_scenic_score_down(treeGrid, treePos):
    scenicScore, x, y = 0, treePos[0], treePos[1]
    tree = treeGrid[x][y]
    for r in range(x+1, len(treeGrid)):
        scenicScore += 1
        if treeGrid[r][y] >= tree:
            break
    return scenicScore


def calculate_scenic_score_up(treeGrid, treePos):
    scenicScore, x, y = 0, treePos[0], treePos[1]
    tree = treeGrid[x][y]
    for r in range(x-1, -1, -1):
        scenicScore += 1
        if treeGrid[r][y] >= tree:
            break
    return scenicScore


def calculate_scenic_score_right(treeGrid, treePos):
    scenicScore, x, y = 0, treePos[0], treePos[1]
    tree = treeGrid[x][y]
    for r in range(y+1, len(treeGrid)):
        scenicScore += 1
        if treeGrid[x][r] >= tree:
            break
    return scenicScore


def calculate_scenic_score_left(treeGrid, treePos):
    scenicScore, x, y = 0, treePos[0], treePos[1]
    tree = treeGrid[x][y]
    for r in range(y-1, -1, -1):
        scenicScore += 1
        if treeGrid[x][r] >= tree:
            break
    return scenicScore


treeGrid = create_grid()
# Part1
totalTrees = 0
for x, row in enumerate(treeGrid):
    if x == 0 or x == len(treeGrid) - 1:
        continue
    for y, tree in enumerate(row):
        if y == 0 or y == len(treeGrid) - 1:
            continue
        treePos = [x, y]
        if scan_horizontally(treeGrid, treePos) and scan_vertically(treeGrid, treePos):
            totalTrees += 1

totalTrees = len(treeGrid)**2 - totalTrees
print(totalTrees)

# Part2
maxScenicScore = 0
for x, row in enumerate(treeGrid):
    for y, tree in enumerate(row):
        treePos = [x, y]
        scenicScore = calculate_scenic_score_up(treeGrid, treePos)*calculate_scenic_score_left(treeGrid, treePos)*calculate_scenic_score_down(treeGrid, treePos)*calculate_scenic_score_right(treeGrid, treePos)
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore

print(maxScenicScore)
