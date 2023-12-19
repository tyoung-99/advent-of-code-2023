# Day 10

import sys


def part_1():
    coords = []
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == "S":
                coords = [
                    {"old": {"x": x, "y": y}, "new": {"x": x, "y": y}},
                    {"old": {"x": x, "y": y}, "new": {"x": x, "y": y}},
                ]
                break
        else:
            continue
        break

    done = False
    if (
        not done and puzzle[coords[0]["old"]["y"] - 1][coords[0]["old"]["x"]] in "|7F"
    ):  # Above
        if coords[0] == coords[1]:
            coords[0]["new"]["y"] = coords[0]["new"]["y"] - 1
        else:
            coords[1]["new"]["y"] = coords[1]["new"]["y"] - 1
            done = True
    if (
        not done and puzzle[coords[0]["old"]["y"] + 1][coords[0]["old"]["x"]] in "|LJ"
    ):  # Below
        if coords[0] == coords[1]:
            coords[0]["new"]["y"] = coords[0]["new"]["y"] + 1
        else:
            coords[1]["new"]["y"] = coords[1]["new"]["y"] + 1
            done = True
    if (
        not done and puzzle[coords[0]["old"]["y"]][coords[0]["old"]["x"] - 1] in "-LF"
    ):  # Left
        if coords[0] == coords[1]:
            coords[0]["new"]["x"] = coords[0]["new"]["x"] - 1
        else:
            coords[1]["new"]["x"] = coords[1]["new"]["x"] - 1
            done = True
    if (
        not done and puzzle[coords[0]["old"]["y"]][coords[0]["old"]["x"] + 1] in "-J7"
    ):  # Right
        if coords[0] == coords[1]:
            coords[0]["new"]["x"] = coords[0]["new"]["x"] + 1
        else:
            coords[1]["new"]["x"] = coords[1]["new"]["x"] + 1
            done = True

    steps = 1
    while coords[0]["new"] != coords[1]["new"]:
        for coord in coords:
            x = coord["new"]["x"]
            y = coord["new"]["y"]
            match puzzle[y][x]:
                case "|":
                    next_coord = {"x": x, "y": y + 1}
                    if next_coord == coord["old"]:
                        next_coord = {"x": x, "y": y - 1}
                case "-":
                    next_coord = {"x": x + 1, "y": y}
                    if next_coord == coord["old"]:
                        next_coord = {"x": x - 1, "y": y}
                case "L":
                    next_coord = {"x": x, "y": y - 1}
                    if next_coord == coord["old"]:
                        next_coord = {"x": x + 1, "y": y}
                case "J":
                    next_coord = {"x": x, "y": y - 1}
                    if next_coord == coord["old"]:
                        next_coord = {"x": x - 1, "y": y}
                case "7":
                    next_coord = {"x": x, "y": y + 1}
                    if next_coord == coord["old"]:
                        next_coord = {"x": x - 1, "y": y}
                case "F":
                    next_coord = {"x": x, "y": y + 1}
                    if next_coord == coord["old"]:
                        next_coord = {"x": x + 1, "y": y}
            coord["old"] = coord["new"]
            coord["new"] = next_coord
        steps += 1

    print(f"Number of steps: {steps}")


def part_2():
    def copy_cell(x: int, y: int, cell_val=None):
        if not cell_val:
            cell_val = puzzle[y][x]
        expanded_puzzle[y * 3 + 1][x * 3 + 1] = cell_val
        above = "."
        below = "."
        left = "."
        right = "."
        if cell_val in "|LJ":
            above = "|"
        if cell_val in "|F7":
            below = "|"
        if cell_val in "-J7":
            left = "-"
        if cell_val in "-FL":
            right = "-"
        expanded_puzzle[y * 3][x * 3 + 1] = above
        expanded_puzzle[y * 3 + 2][x * 3 + 1] = below
        expanded_puzzle[y * 3 + 1][x * 3] = left
        expanded_puzzle[y * 3 + 1][x * 3 + 2] = right

    def fill_outer(start_x, start_y):
        expanded_puzzle[start_y][start_x] = "O"
        if (
            start_x < len(expanded_puzzle[0]) - 1
            and expanded_puzzle[start_y][start_x + 1] == "."
        ):
            fill_outer(start_x + 1, start_y)
        if start_x > 0 and expanded_puzzle[start_y][start_x - 1] == ".":
            fill_outer(start_x - 1, start_y)
        if (
            start_y < len(expanded_puzzle) - 1
            and expanded_puzzle[start_y + 1][start_x] == "."
        ):
            fill_outer(start_x, start_y + 1)
        if start_y > 0 and expanded_puzzle[start_y - 1][start_x] == ".":
            fill_outer(start_x, start_y - 1)

    for i, line in enumerate(puzzle):
        puzzle[i] = line.strip()
    expanded_puzzle = [
        ["." for _ in range(len(puzzle[0]) * 3)] for _ in range(len(puzzle * 3))
    ]

    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == "S":
                start = {"x": x, "y": y}
                break
        else:
            continue
        break

    if puzzle[start["y"] - 1][start["x"]] in "|7F":  # Above
        second = {"x": start["x"], "y": start["y"] - 1}
    elif puzzle[start["y"] + 1][start["x"]] in "|LJ":  # Below
        second = {"x": start["x"], "y": start["y"] + 1}
    else:
        second = {"x": start["x"] - 1, "y": start["y"]}

    copy_cell(second["x"], second["y"])
    current = {
        "old": {"x": start["x"], "y": start["y"]},
        "new": {"x": second["x"], "y": second["y"]},
    }

    while current["new"] != start:
        x = current["new"]["x"]
        y = current["new"]["y"]
        match puzzle[y][x]:
            case "|":
                next_coord = {"x": x, "y": y + 1}
                if next_coord == current["old"]:
                    next_coord = {"x": x, "y": y - 1}
            case "-":
                next_coord = {"x": x + 1, "y": y}
                if next_coord == current["old"]:
                    next_coord = {"x": x - 1, "y": y}
            case "L":
                next_coord = {"x": x, "y": y - 1}
                if next_coord == current["old"]:
                    next_coord = {"x": x + 1, "y": y}
            case "J":
                next_coord = {"x": x, "y": y - 1}
                if next_coord == current["old"]:
                    next_coord = {"x": x - 1, "y": y}
            case "7":
                next_coord = {"x": x, "y": y + 1}
                if next_coord == current["old"]:
                    next_coord = {"x": x - 1, "y": y}
            case "F":
                next_coord = {"x": x, "y": y + 1}
                if next_coord == current["old"]:
                    next_coord = {"x": x + 1, "y": y}
        current["old"] = current["new"]
        current["new"] = next_coord
        copy_cell(current["old"]["x"], current["old"]["y"])

    if second["x"] > start["x"] or current["old"]["x"] > start["x"]:
        if second["y"] > start["y"] or current["old"]["y"] > start["y"]:
            char = "F"
        elif second["y"] < start["y"] or current["old"]["y"] < start["y"]:
            char = "L"
        else:
            char = "-"
    elif second["x"] < start["x"] or current["old"]["x"] < start["x"]:
        if second["y"] > start["y"] or current["old"]["y"] > start["y"]:
            char = "7"
        else:  # No need to check for < y vs == y, == y caught in 1st if
            char = "J"
    else:
        char = "|"
    copy_cell(start["x"], start["y"], char)

    sys.setrecursionlimit(99999)
    fill_outer(0, 0)

    enclosed_tiles = 0
    for y in range(1, len(expanded_puzzle), 3):
        for x in range(1, len(expanded_puzzle[y]), 3):
            if expanded_puzzle[y][x] == ".":
                enclosed_tiles += 1

    # for line in expanded_puzzle:
    #     for char in line:
    #         print(char, end="")
    #     print()

    print(f"Tiles enclosed by loop: {enclosed_tiles}")


with open("src/day_10/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_2()
