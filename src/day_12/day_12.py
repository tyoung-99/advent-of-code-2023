# Day 12

from itertools import product
import re


def part_1(puzzle):
    def find_combos(spring_data):
        combos = set()

        springs, groups = spring_data
        possible_chars = []
        for spring in springs:
            if spring == "?":
                possible_chars.append(["#", "."])
            else:
                possible_chars.append([spring])

        for combo in product(*possible_chars):
            combo = "".join(combo)
            test_groups = re.findall(r"#+", combo)
            test_groups = [len(group) for group in test_groups]
            if test_groups == groups:
                combos.add(combo)

        return len(combos)

    springs = [line.strip().split() for line in puzzle]
    springs = [
        [line[0], [int(group) for group in line[1].split(",")]] for line in springs
    ]
    combos = [find_combos(data) for data in springs]

    # print(combos)
    print(f"Sum of counts: {sum(combos)}")


with open("src/day_12/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_1(puzzle)
print()
