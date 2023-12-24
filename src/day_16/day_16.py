# Day 16

import sys


def part_1(puzzle):
    def out_of_bounds(beam):
        if 0 <= beam["y"] < len(energized) and 0 <= beam["x"] < len(energized[0]):
            return False
        return True

    def energize(beam, tile):
        if beam["x_change"] == -1:
            if tile["neg_x"]:
                return True
            tile["neg_x"] = True
        elif beam["x_change"] == 1:
            if tile["pos_x"]:
                return True
            tile["pos_x"] = True
        elif beam["y_change"] == -1:
            if tile["neg_y"]:
                return True
            tile["neg_y"] = True
        elif beam["y_change"] == 1:
            if tile["pos_y"]:
                return True
            tile["pos_y"] = True
        return False

    def get_new_beams(beam, tile_type):
        new_beam = None

        match tile_type:
            case ".":
                beam["x"] += beam["x_change"]
                beam["y"] += beam["y_change"]
            case "/":
                beam["x_change"], beam["y_change"] = (
                    -1 * beam["y_change"],
                    -1 * beam["x_change"],
                )
                beam["x"] += beam["x_change"]
                beam["y"] += beam["y_change"]
            case "\\":
                beam["x_change"], beam["y_change"] = beam["y_change"], beam["x_change"]
                beam["x"] += beam["x_change"]
                beam["y"] += beam["y_change"]
            case "|":
                if beam["x_change"] == 0:
                    beam["y"] += beam["y_change"]
                else:
                    new_beam = {
                        "x": beam["x"],
                        "y": beam["y"] + 1,
                        "x_change": 0,
                        "y_change": 1,
                    }
                    beam["y"] -= 1
                    beam["x_change"] = 0
                    beam["y_change"] = -1

            case "-":
                if beam["y_change"] == 0:
                    beam["x"] += beam["x_change"]
                else:
                    new_beam = {
                        "x": beam["x"] + 1,
                        "y": beam["y"],
                        "x_change": 1,
                        "y_change": 0,
                    }
                    beam["x"] -= 1
                    beam["x_change"] = -1
                    beam["y_change"] = 0

        return beam, new_beam

    def traverse(beam):
        if out_of_bounds(beam):
            return

        tile = energized[beam["y"]][beam["x"]]
        tile_type = puzzle[beam["y"]][beam["x"]]

        if energize(beam, tile):
            return

        beam, new_beam = get_new_beams(beam, tile_type)
        traverse(beam)
        if new_beam:
            traverse(new_beam)

    energized = [
        [
            {
                "pos_x": False,
                "neg_x": False,
                "pos_y": False,
                "neg_y": False,
            }
            for _ in line.strip()
        ]
        for line in puzzle
    ]
    sys.setrecursionlimit(2000)
    traverse({"x": 0, "y": 0, "x_change": 1, "y_change": 0})

    energized_count = 0
    for line in energized:
        for tile in line:
            energized = "."
            if any(tile[dir] for dir in tile):
                energized = "#"
                energized_count += 1
            # print(energized, end="")
        # print()

    print(f"Tiles energized: {energized_count}")


with open("src/day_16/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_1(puzzle)
