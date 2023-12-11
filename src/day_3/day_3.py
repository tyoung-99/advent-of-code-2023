# Day 3

def part_1():
    def is_adjacent(num, symbol):
        if num["added"]:
            return False
        if num["x"] - 1 <= symbol["x"] <= num["x"] + len(str(num["val"])):
            if num["y"] - 1 <= symbol["y"] <= num["y"] + 1:
                num["added"] = True
                return True
        return False

    input_file = open("src/day_3/puzzle_input.txt", "r", encoding="utf-8")
    schematic = input_file.readlines()
    nums = [[] for i in range(len(schematic))]
    symbols = [[] for i in range(len(schematic))]
    part_nums = []

    for y, line in enumerate(schematic):
        line = line.strip()
        building_num = ""
        for x, char in enumerate(line):
            if char.isnumeric():
                building_num += char
            else:
                if building_num != "":
                    nums[y].append({"val": int(building_num), "x": x - len(building_num), "y": y, "added": False})
                    building_num = ""
                if char != ".":
                    symbols[y].append({"symbol": char, "x": x, "y": y})

        if building_num != "":
            nums[y].append({"val": int(building_num), "x": len(line) - len(building_num), "y": y, "added": False})

    for y, line in enumerate(symbols):
        if line:
            for symbol in line:
                for new_y in range(y-1, y+2):
                    for num in nums[new_y]:
                        if is_adjacent(num, symbol):
                            part_nums.append(num["val"])

    # print(part_nums)
    print(f"Sum of all part numbers: {sum(part_nums)}")

def part_2():
    def is_adjacent(num, symbol):
        if num["x"] - 1 <= symbol["x"] <= num["x"] + len(str(num["val"])):
            if num["y"] - 1 <= symbol["y"] <= num["y"] + 1:
                return True
        return False

    input_file = open("src/day_3/puzzle_input.txt", "r", encoding="utf-8")
    schematic = input_file.readlines()
    nums = [[] for i in range(len(schematic))]
    symbols = [[] for i in range(len(schematic))]
    gear_ratios = []

    for y, line in enumerate(schematic):
        line = line.strip()
        building_num = ""
        for x, char in enumerate(line):
            if char.isnumeric():
                building_num += char
            else:
                if building_num != "":
                    nums[y].append({"val": int(building_num), "x": x - len(building_num), "y": y})
                    building_num = ""
                if char != ".":
                    symbols[y].append({"symbol": char, "x": x, "y": y})

        if building_num != "":
            nums[y].append({"val": int(building_num), "x": len(line) - len(building_num), "y": y})

    for y, line in enumerate(symbols):
        if line:
            for symbol in line:
                adjacents = []
                for new_y in range(y-1, y+2):
                    for num in nums[new_y]:
                        if is_adjacent(num, symbol):
                            adjacents.append(num["val"])
                if len(adjacents) == 2:
                    gear_ratios.append(adjacents[0] * adjacents[1])

    # print(gear_ratios)
    print(f"Sum of all gear ratios: {sum(gear_ratios)}")

part_2()
