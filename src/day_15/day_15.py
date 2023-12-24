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


def part_2(puzzle):
    def box_hash(code):
        final = 0
        for char in code:
            final += ord(char)
            final *= 17
            final %= 256
        return final

    steps = puzzle.split(",")
    boxes = [[] for _ in range(256)]
    for step in steps:
        try:
            split = step.index("=")
            focal_length = int(step[split + 1 :])
        except ValueError:
            split = step.index("-")

        label = step[:split]
        box_num = box_hash(label)
        operator = step[split]

        box = boxes[box_num]
        if operator == "-":
            for i, lens in enumerate(box):
                if lens["label"] == label:
                    boxes[box_num] = box[:i] + box[i + 1 :]
                    break
            continue

        found = False
        for i, lens in enumerate(box):
            if lens["label"] == label:
                box[i]["focal_length"] = focal_length
                found = True
                break
        if not found:
            box.append({"label": label, "focal_length": focal_length})

    focusing_powers = []
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focusing_powers.append((i + 1) * (j + 1) * lens["focal_length"])

    # print(focusing_powers)
    print(f"Sum of focusing powers: {sum(focusing_powers)}")


with open("src/day_15/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readline()
part_2(puzzle)
