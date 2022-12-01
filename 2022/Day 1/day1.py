with open("2022\Day 1\data\day1.csv", "r") as f:
    elfList = []
    currentElf = 0
    for i, line in enumerate(f):
        if line.strip():
            currentElf += int(line.strip())
        else:
            elfList.append(currentElf)
            currentElf = 0
    partOneSolution = sorted(elfList,reverse=True)[0]
    partTwoSolution = sum(sorted(elfList,reverse=True)[:3])
    print("Part 1: " + str(partOneSolution))
    print("Part 2: " + str(partTwoSolution))