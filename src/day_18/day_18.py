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


def part_2(puzzle):
    def clear_area(y_start, y_stop, zones):
        cleared = 0
        # print(y_start, y_stop)
        for x_start, x_stop in zones:
            # print(x_start, x_stop)
            cleared += (x_stop - x_start + 1) * (y_stop - y_start + 1)
            # print(cleared)
        # print()
        return cleared

    def print_lagoon(h_lines):
        max_x, max_y = 0, 0
        for line in h_lines:
            if line[0] > max_x:
                max_x = line[0]
            if line[1] > max_x:
                max_x = line[1]
            if line[2] > max_y:
                max_y = line[2]
        lagoon = np.array([["."] * (max_x + 1) for _ in range(max_y + 1)])
        for y, _ in enumerate(lagoon):
            for h_line in h_lines:
                if y == h_line[2]:
                    for x in range(h_line[0], h_line[1] + 1):
                        lagoon[y][x] = "#"
        print(lagoon)

    def update_clearing(clearing, h_lines, y):
        # Area removed from clearing must be returned to account for it, not accounted for in next clear
        removed = 0
        for line in h_lines:
            if line[2] != y:
                continue

            disconnected = True
            for i, (x_start, x_stop) in enumerate(clearing):
                if line[0] > x_stop or line[1] < x_start:
                    continue

                disconnected = False

                # Extend clearing
                if line[0] == x_stop:
                    if i < len(clearing) - 1 and line[1] == clearing[i + 1][0]:
                        clearing[i] = (x_start, clearing[i + 1][1])
                        del clearing[i + 1]
                        break
                    clearing[i] = (x_start, line[1])
                    break
                if line[1] == x_start:
                    clearing[i] = (line[0], x_stop)
                    break

                # Reduce clearing
                removed += line[1] - line[0] - 1
                if line[0] == x_start:
                    if line[1] == x_stop:
                        removed += 2  # Account for both corners
                        del clearing[i]
                        break
                    removed += 1  # 1 corner
                    clearing[i] = (line[1], x_stop)
                    break
                if line[1] == x_stop:
                    removed += 1  # 1 corner
                    clearing[i] = (x_start, line[0])
                    break

                clearing[i] = (x_start, line[0])
                clearing.insert(i + 1, (line[1], x_stop))
                break

            if disconnected:
                clearing.append((line[0], line[1]))
                clearing = sorted(clearing, key=lambda x: x[0])

        # print(clearing)
        return clearing, removed

    h_lines, x, y = [], 0, 0
    for line in puzzle:
        line = line.split()
        n = int(line[2][2:7], 16)
        match line[2][7]:
            case "0":
                h_lines.append((x, x + n, y))
                x += n
            case "1":
                y += n
            case "2":
                h_lines.append((x - n, x, y))
                x -= n
            case "3":
                y -= n

    # h_lines = [(0, 9, -1), (5, 9, 9), (0, 3, 9), (5, 7, 5), (3, 7, 3)]
    # print_lagoon(h_lines)

    h_bars = sorted({h_line[2] for h_line in h_lines})

    cleared = 0
    clearing = []
    clear_from = h_bars[0]
    for y in h_bars:
        if clearing:
            cleared += clear_area(clear_from, y - 1, clearing)
            # print(f"Cleared: {cleared}")
            clear_from = y
        new_clearing, extra_cleared = update_clearing(clearing, h_lines, y)
        clearing = new_clearing
        cleared += extra_cleared
        # print(f"Extra Cleared: {extra_cleared}")

    print(f"Cubic meters: {cleared}")


with open("src/day_18/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_2(puzzle)
