outcomes1 = {"A X": 4,
             "A Y": 8,
             "A Z": 3,
             "B X": 1,
             "B Y": 5,
             "B Z": 9,
             "C X": 7,
             "C Y": 2,
             "C Z": 6}

outcomes2 = {"A X": 3,
             "A Y": 4,
             "A Z": 8,
             "B X": 1,
             "B Y": 5,
             "B Z": 9,
             "C X": 2,
             "C Y": 6,
             "C Z": 7}


def calculate_outcome(outcomes):
    score = 0
    with open("input.txt", "r+") as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip("\n")
            score += outcomes[line]
    return score


print(calculate_outcome(outcomes1))
print(calculate_outcome(outcomes2))
