# Day 14


def part_1(puzzle):
    platform = [[x for x in row.strip()] for row in puzzle]
    total_load = 0

    for x, _ in enumerate(platform[0]):
        stop_point = 0
        for y, row in enumerate(platform):
            if row[x] == "#":
                stop_point = y + 1
            elif row[x] == "O":
                platform[y][x] = "."
                platform[stop_point][x] = "O"
                total_load += len(platform) - stop_point
                stop_point += 1

    print(f"Total load: {total_load}")


with open("src/day_14/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_1(puzzle)
