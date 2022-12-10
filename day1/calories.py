curSum, maxSum = 0, -1
with open("calories_input.txt", "r+") as file:
    lines = file.readlines()
    for line in lines:
        if line == "\n":
            maxSum = max(maxSum, curSum)
            curSum = 0
        else:
            curSum += int(line)
print(maxSum)

sums, total = [], 0
for line in lines:
    if line == "\n":
        sums.append(total)
        total = 0
    else:
        total += int(line)
sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])
