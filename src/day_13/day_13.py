# Day 13


def part_1(puzzle):
    def check_reflect(pattern, row=0, col=0):
        if row:
            small_side = row
            if len(pattern) - row < small_side:
                small_side = len(pattern) - row

            for gap in range(small_side):
                if pattern[row - 1 - gap] != pattern[row + gap]:
                    return False
            return row * 100

        small_side = col
        if len(pattern[0]) - col < small_side:
            small_side = len(pattern[0]) - col

        for gap in range(small_side):
            for line in pattern:
                if line[col - 1 - gap] != line[col + gap]:
                    return False
        return col

    patterns = [pattern.split("\n") for pattern in puzzle.split("\n\n")]
    reflection_counts = []

    for pattern in patterns:
        for row in range(1, len(pattern)):
            count = check_reflect(pattern, row=row)
            if count:
                reflection_counts.append(count)
                break
        if not count:
            for col in range(1, len(pattern[0])):
                count = check_reflect(pattern, col=col)
                if count:
                    reflection_counts.append(count)
                    break

    print(reflection_counts)
    print(f"Pattern summary: {sum(reflection_counts)}")


with open("src/day_13/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.read()
part_1(puzzle)
