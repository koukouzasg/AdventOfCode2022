from anytree import Node, PreOrderIter


def read_file(path):
    with open(path, "r+") as file:
        lines = file.readlines()
    return [line.rstrip("\n") for line in lines]


def calculate(node):
    total = 0
    if hasattr(node, "fileSize"):
        return int(node.fileSize)
    else:
        for child in node.children:
            total += calculate(child)
    return total


commands = read_file("input.txt")
root, commands = Node("/"), commands[1:]
currentDir, prevDir, visited = root, root, {"/": root}

for command in commands:
    info = command.split()
    if info[0] == '$':
        if info[1] == "ls":
            continue
        else:
            if info[2] == "..":
                currentDir = currentDir.parent
                prevDir = currentDir.parent
            else:
                prevDir = visited[currentDir.name]
                route = "/"
                for n in currentDir.path:
                    route += n.name + "/"
                route = route + info[2]
                currentDir = visited[route]
    elif info[0] == "dir":
        route = "/"
        for n in currentDir.path:
            route += n.name + "/"
        route = route + info[1]
        visited[route] = Node(route, parent=currentDir)
    else:
        route = "/"
        for n in currentDir.path:
            route += n.name + "/"
        route = route + info[1]
        visited[route] = Node(route, parent=currentDir, fileSize=int(info[0]))

totalSum = 0
dirSums = {}
for node in PreOrderIter(root):
    if node.children:
        dirSum = calculate(node)
        dirSums[node.name] = dirSum
        if dirSum <= 100000:
            totalSum += dirSum
print(totalSum)

used = dirSums["/"]
needed = 70000000 - used
updateNeeded = 30000000 - needed
deleteDirs = []
for key in dirSums:
    if dirSums[key] >= updateNeeded:
        deleteDirs.append(dirSums[key])
deleteDirs.sort()
print(deleteDirs[0])