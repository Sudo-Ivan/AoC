def day1_function():
    with open("input.txt") as f:
        a = []
        b = 0
        for i, line in enumerate(f):
            if line.strip():
                b += int(line.strip())
            else:
                a.append(b)
                b = 0
        p1 = sorted(a,reverse=True)[0]
        p2 = sum(sorted(a,reverse=True)[:3])
        print("Part 1: " + str(p1))
        print("Part 2: " + str(p2))  
day1_function()