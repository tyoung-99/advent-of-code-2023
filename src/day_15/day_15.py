# Day 15


def part_1(puzzle):
    steps = puzzle.split(",")
    step_hashes = []
    for step in steps:
        step_hashes.append(0)
        for char in step:
            step_hashes[-1] += ord(char)
            step_hashes[-1] *= 17
            step_hashes[-1] %= 256

    # print(step_hashes)
    print(f"Sum of results: {sum(step_hashes)}")


with open("src/day_15/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readline()
part_1(puzzle)
