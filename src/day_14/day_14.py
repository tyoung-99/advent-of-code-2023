# Day 14

import numpy as np


def part_1(puzzle):
    platform = [list(row.strip()) for row in puzzle]
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


def part_2(puzzle):
    def print_plat(platform):
        for line in platform:
            for char in line:
                print(char, end="")
            print()
        print()

    def calc_load(platform):
        load = 0
        for y, row in enumerate(platform):
            for cell in row:
                if cell == "O":
                    load += len(platform) - y
        return load

    def spin_cycle(platform):
        for _ in range(4):
            platform = np.rot90(platform)
            tilt(platform)

    def tilt(platform):
        for offset in range(1, platform.shape[0]):
            for row in range(platform.shape[0] - offset):
                selection = (platform[row, :] == ".") & (platform[row + 1, :] == "O")
                platform[row, selection] = "O"
                platform[row + 1, selection] = "."

    platform = np.genfromtxt(
        "src/day_14/ex_puzzle_input.txt", dtype=bytes, comments=None, delimiter=1
    ).astype(str)

    cycles_seen = {}
    MAX_CYCLES = 1000000000
    cycles_completed = 0
    while cycles_completed < MAX_CYCLES:
        spin_cycle(platform)
        key = hash(platform.data.tobytes())
        if key in cycles_seen:
            cycles_completed = MAX_CYCLES - (MAX_CYCLES - cycles_completed) % (
                cycles_completed - cycles_seen[key]
            )
        else:
            cycles_seen[key] = cycles_completed
        cycles_completed += 1

    print_plat(platform)

    print(f"Total load: {calc_load(platform)}")


with open("src/day_14/ex_puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_2(puzzle)
