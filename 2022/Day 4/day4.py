# Parse the input to extract the ranges of section IDs
pairs = []
with open("input.txt") as f:
    for line in f:
        a, b = line.strip().split(",")
        pairs.append((a, b))

# Iterate through each pair and check for fully contained ranges
counter = 0
for a, b in pairs:
    a_start, a_end = map(int, a.split("-"))
    b_start, b_end = map(int, b.split("-"))
    if (a_start <= b_start and a_end >= b_end) or (b_start <= a_start and b_end >= a_end):
        counter += 1

# Print the result
print(counter)

R = 100

def split(e):
    return tuple(int(x) for x in e.split('-'))


def contains(range1, range2):
    rooms = [0] * R
    for room in range(range1[0], range1[1]+1):
        rooms[room] += 1
    for room in range(range2[0], range2[1]+1):
        rooms[room] += 1
    return any(room == 2 for room in rooms)


contained = 0
with open('input.txt') as f:
    for line in f:
        elves = line.strip().split(',')
        if contains(split(elves[0]), split(elves[1])):
            contained += 1

print(contained)