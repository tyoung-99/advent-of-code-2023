# Day 19


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


with open("src/day_19/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.read()
part_1(puzzle)
