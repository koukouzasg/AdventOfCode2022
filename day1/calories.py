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

sums, sum = [], 0
for line in lines:
    if line == "\n":
        sums.append(sum)
        sum = 0
    else:
        sum += int(line)
sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])
