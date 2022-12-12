def read_file(path):
    with open(path, "r+") as file:
        lines = file.readlines()
    return [line.rstrip("\n") for line in lines]


def ovelaps1(start1: int, end1: int, start2: int, end2: int) -> bool:
    return start1 <= start2 and end2 <= end1


def ovelaps2(start1: int, end1: int, start2: int, end2: int) -> bool:
    return (start1 <= start2 and end2 <= end1) or (start2 <= end1 <= end2) or (start2 <= start1 <= end2)


lines = read_file("input.txt")
totalSum1 = 0
totalSum2 = 0
for line in lines:
    section1, section2 = line.split(",")
    s1, e1 = section1.split("-")
    s2, e2 = section2.split("-")
    if ovelaps1(int(s1), int(e1), int(s2), int(e2)) or ovelaps1(int(s2), int(e2), int(s1), int(e1)):
        totalSum1 += 1
    if ovelaps2(int(s1), int(e1), int(s2), int(e2)) or ovelaps2(int(s2), int(e2), int(s1), int(e1)):
        totalSum2 += 1

print(totalSum1, totalSum2)
