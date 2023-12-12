# Day 5

def part_1():
    input_file = open("src/day_5/puzzle_input.txt", "r", encoding="utf-8")
    lines = input_file.readlines()
    data = []
    conversions = []

    for line in lines:
        if ":" in line:
            if not data:
                _, seeds = line.split(": ")
                data = seeds.split()
                data = [ int(x) for x in data ]

        elif line == "\n":
            for i, item in enumerate(data):
                for convert in conversions:
                    if convert["src_start"] <= item < convert["src_start"] + convert["length"]:
                        data[i] = item + convert["dest_start"] - convert["src_start"]
            conversions = []

        else:
            temp_data = line.split()
            temp_data = [ int(x) for x in temp_data ]
            dest_start, src_start, length = temp_data
            conversions.append({"dest_start": dest_start, "src_start": src_start, "length": length})

    # Data goes to end of file
    for i, item in enumerate(data):
        for convert in conversions:
            if convert["src_start"] <= item < convert["src_start"] + convert["length"]:
                data[i] = item + convert["dest_start"] - convert["src_start"]

    # print(data)
    print(f"Lowest location: {min(data)}")


part_1()
