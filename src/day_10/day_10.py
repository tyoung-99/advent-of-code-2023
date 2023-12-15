# Day 10


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


with open("src/day_10/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_1()
