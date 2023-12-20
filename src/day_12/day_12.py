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


def part_2(puzzle):
    def handle_broken(springs, groups):
        next_group = groups[0]
        cut = springs[:next_group]
        delimiter = springs[next_group] if next_group < len(springs) else None
        if delimiter == "#" or "." in cut:
            return 0
        else:
            return find_combos(springs[next_group + 1 :], groups[1:])

    def handle_working(springs, groups):
        return find_combos(springs[1:], groups)

    def find_combos(springs, groups):
        key = (springs, tuple(groups))
        if key in combos_seen:
            return combos_seen[key]
        if sum(groups) + len(groups) - 1 > len(springs):
            result = 0
        elif groups == []:
            if any(spring == "#" for spring in springs):
                result = 0
            else:
                result = 1
        elif springs[0] == "#":
            result = handle_broken(springs, groups)
        elif springs[0] == ".":
            result = handle_working(springs, groups)
        elif springs[0] == "?":
            result = handle_broken(springs, groups) + handle_working(springs, groups)

        combos_seen[key] = result
        return result

    combos = []
    combos_seen = {}
    for line in puzzle:
        springs, groups = line.strip().split()
        groups = [int(x) for x in groups.split(",")]
        springs = "?".join([springs] * 5)
        groups *= 5
        combos.append(find_combos(springs, groups))

    # print(combos)
    print(f"Sum of counts: {sum(combos)}")


with open("src/day_12/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_2(puzzle)
