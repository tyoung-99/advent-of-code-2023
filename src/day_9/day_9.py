# Day 9


def part_1():
    readings = []
    for line in puzzle:
        reading_set = []
        reading_set.append([int(x) for x in line.split()])
        readings.append(reading_set)

    for reading_set in readings:
        differences = reading_set[0]
        while any(item != 0 for item in differences):
            differences = []
            for i, reading in enumerate(reading_set[0]):
                if i == 0:
                    continue
                differences.append(reading - reading_set[0][i - 1])
            reading_set.insert(0, differences)

    sum = 0
    for reading_set in readings:
        for i, reading in enumerate(reading_set):
            # Don't actually need to update 1st set, since new val will be 0 like current last val
            if i == 0:
                continue
            reading.append(reading[-1] + reading_set[i - 1][-1])
        sum += reading[-1]

    print(f"Sum of next values: {sum}")


with open("src/day_9/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_1()
