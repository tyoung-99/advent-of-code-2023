# Day 8

import re


def part_1():
    input_file = open("src/day_8/puzzle_input.txt", "r", encoding="utf-8")
    steps = input_file.readlines()
    nodes = steps[2:]
    steps = steps[0].strip()

    new_nodes = {}
    for line in nodes:
        line = re.sub(r" = \(|, |\)", " ", line)
        line = line.split()
        new_nodes[line[0]] = {"L": line[1], "R": line[2]}
    nodes = new_nodes

    current = "AAA"
    step_count = 0
    step_index = 0
    while current != "ZZZ":
        current = nodes[current][steps[step_index]]
        step_count += 1
        step_index += 1
        if step_index >= len(steps):
            step_index = 0

    print(f"Steps required: {step_count}")


part_1()
