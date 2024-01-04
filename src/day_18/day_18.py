# Day 18

import numpy as np


def part_1(puzzle):
    def print_lagoon(lagoon):
        for line in lagoon:
            for char in line:
                print(char, end="")
            print()
        print()

    def draw_outline(puzzle, lagoon):
        row, col = (int(len(lagoon) / 2), int(len(lagoon) / 2))

        while lagoon[row][col] != "#":
            direction, distance, _ = puzzle.pop(0).split()
            distance = int(distance)

            if direction in ("L", "R"):
                lagoon = np.transpose(lagoon)
                row, col = col, row

            for _ in range(distance):
                lagoon[row][col] = "#"
                row += DIRECTIONS[direction]

                if not (0 <= row < len(lagoon) and 0 <= col < len(lagoon[0])):
                    if direction in ("U", "L"):
                        lagoon = np.insert(lagoon, 0, [["."] * len(lagoon[0])], 0)
                        row += 1
                    else:
                        lagoon = np.append(lagoon, [["."] * len(lagoon[0])], 0)

            if direction in ("L", "R"):
                lagoon = np.transpose(lagoon)
                row, col = col, row

        print_lagoon(lagoon)
        return lagoon

    def fill_outside(lagoon):
        lagoon = np.insert(lagoon, 0, [["."] * len(lagoon[0])], 0)
        lagoon = np.insert(lagoon, 0, [["."] * len(lagoon)], 1)
        lagoon = np.append(lagoon, [["."] * len(lagoon[0])], 0)
        lagoon = np.append(lagoon, [["."]] * len(lagoon), 1)

        stack = [(0, 0)]
        while stack:
            row, col = stack.pop()

            if lagoon[row][col] == ".":
                lagoon[row][col] = "O"
                stack.extend(get_neighbors(lagoon.shape, (row, col)))

        print_lagoon(lagoon)
        return lagoon

    def get_neighbors(shape, coords):
        neighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                new_coords = (coords[0] + i, coords[1] + j)
                if (
                    0 <= new_coords[0] < shape[0]
                    and 0 <= new_coords[1] < shape[1]
                    and new_coords != coords
                ):
                    neighbors.append(new_coords)

        return neighbors

    def count_inside(lagoon):
        unique, counts = np.unique(lagoon, return_counts=True)
        tiles = dict(zip(unique, counts))
        return tiles["#"] + tiles["."]

    DIRECTIONS = {"U": -1, "D": 1, "L": -1, "R": 1}
    lagoon = np.array([["."] * 10 for _ in range(10)])
    lagoon = draw_outline(puzzle, lagoon)
    lagoon = fill_outside(lagoon)
    print(f"Cubic meters of lava: {count_inside(lagoon)}")


with open("src/day_18/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_1(puzzle)
