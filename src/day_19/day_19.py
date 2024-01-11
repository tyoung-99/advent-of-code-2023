# Day 19

from copy import deepcopy


def part_1(puzzle):
    def parse_puzzle(puzzle):
        workflows_raw, parts = puzzle.split("\n\n")

        workflows_raw = workflows_raw.split()
        workflows = {}
        for workflow in workflows_raw:
            name, rules = workflow[:-1].split("{")
            rules = [rule.split(":") for rule in rules.split(",")]
            for i, rule in enumerate(rules):
                if len(rule) > 1:
                    rules[i] = [rule[0][0], rule[0][1], int(rule[0][2:]), rule[1]]
            workflows[name] = rules

        parts = parts.split()
        for i, part in enumerate(parts):
            new_part = {}
            ratings = part[1:-1].split(",")
            for val in ratings:
                new_part[val[0]] = int(val[2:])
            parts[i] = new_part

        return workflows, parts

    def check_part(part, workflows):
        name = "in"
        while name not in ["A", "R"]:
            for rule in workflows[name]:
                if len(rule) == 1:
                    name = rule[0]
                    break
                rating = part[rule[0]]
                if (rule[1] == ">" and rating > rule[2]) or (
                    rule[1] == "<" and rating < rule[2]
                ):
                    name = rule[3]
                    break

        if name == "A":
            return True
        return False

    workflows, parts = parse_puzzle(puzzle)
    accepted = []

    for part in parts:
        if check_part(part, workflows):
            accepted.append(part)

    rating_sum = 0
    for part in accepted:
        rating_sum += sum(part.values())

    print(f"Sum of ratings: {rating_sum}")


def part_2(puzzle):
    def parse_puzzle(puzzle):
        workflows_raw, _ = puzzle.split("\n\n")

        workflows_raw = workflows_raw.split()
        workflows = {}
        for workflow in workflows_raw:
            name, rules = workflow[:-1].split("{")
            rules = [rule.split(":") for rule in rules.split(",")]
            for i, rule in enumerate(rules):
                if len(rule) > 1:
                    rules[i] = [rule[0][0], rule[0][1], int(rule[0][2:]), rule[1]]
            workflows[name] = rules

        return workflows

    def get_combinations(
        seen,
        workflows,
        name,
        ranges=None,
    ):
        if ranges is None:
            ranges = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}

        key = tuple((range[0], range[1]) for range in ranges.values())
        if key in seen:
            return seen[key]

        if name == "A":
            combinations = 1
            for range_min, range_max in ranges.values():
                combinations *= range_max - range_min + 1
            seen[key] = combinations
            return combinations
        if name == "R":
            seen[key] = 0
            return 0

        combinations_sum = 0
        for rule in workflows[name]:
            if len(rule) == 1:
                combinations = combinations_sum + get_combinations(
                    seen, workflows, rule[0], ranges
                )
                seen[key] = combinations
                return combinations
            category, sign, compare_to, dest = rule

            if_true = deepcopy(ranges)
            if sign == ">":
                if_true[category] = [compare_to + 1, ranges[category][1]]
                ranges[category] = [ranges[category][0], compare_to]
            else:
                if_true[category] = [ranges[category][0], compare_to - 1]
                ranges[category] = [compare_to, ranges[category][1]]
            combinations = get_combinations(seen, workflows, dest, if_true)
            # seen[key] = combinations
            combinations_sum += combinations

    workflows = parse_puzzle(puzzle)
    seen = {}
    combinations = get_combinations(seen, workflows, "in")

    print(f"Accepted combinations: {combinations}")


with open("src/day_19/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.read()
part_2(puzzle)
