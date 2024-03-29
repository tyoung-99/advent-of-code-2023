# Day 11


def part_1(puzzle):
    def find_path(gal_1, gal_2):
        return abs(gal_1[0] - gal_2[0]) + abs(gal_1[1] - gal_2[1])

    expanded_puzzle = [list(line.strip()) for line in puzzle]
    expand_cols = {x for x, _ in enumerate(expanded_puzzle[0])}
    expand_rows = {y for y, _ in enumerate(expanded_puzzle)}
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == "#":
                expand_cols.discard(x)
                expand_rows.discard(y)

    for x in range(len(expanded_puzzle[0]) - 1, -1, -1):
        if x in expand_cols:
            for y, _ in enumerate(expanded_puzzle):
                expanded_puzzle[y].insert(x, ".")
    for y in range(len(expanded_puzzle) - 1, -1, -1):
        if y in expand_rows:
            expanded_puzzle.insert(y, ["." for i, _ in enumerate(expanded_puzzle[0])])

    galaxies = []
    for y, line in enumerate(expanded_puzzle):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append([x, y])

    path_sum = 0
    for i, galaxy in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            path_sum += find_path(galaxy, galaxies[j])

    print(f"Sum of path lengths: {path_sum}")


def part_2(puzzle):
    def find_path(gal_1, gal_2):
        dist = 0

        if gal_1[0] > gal_2[0]:
            higher = gal_1[0]
            lower = gal_2[0]
        else:
            lower = gal_1[0]
            higher = gal_2[0]

        for x in range(lower, higher):
            if x in expand_cols:
                dist += 1000000
            else:
                dist += 1

        if gal_1[1] > gal_2[1]:
            higher = gal_1[1]
            lower = gal_2[1]
        else:
            lower = gal_1[1]
            higher = gal_2[1]

        for y in range(lower, higher):
            if y in expand_rows:
                dist += 1000000
            else:
                dist += 1

        return dist

    puzzle = [list(line.strip()) for line in puzzle]
    expand_cols = {x for x, _ in enumerate(puzzle[0])}
    expand_rows = {y for y, _ in enumerate(puzzle)}
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == "#":
                expand_cols.discard(x)
                expand_rows.discard(y)

    galaxies = []
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append([x, y])

    path_sum = 0
    for i, galaxy in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            path_sum += find_path(galaxy, galaxies[j])

    print(f"Sum of path lengths: {path_sum}")


with open("src/day_11/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_2(puzzle)
