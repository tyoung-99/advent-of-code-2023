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
                data = [int(x) for x in data]

        elif line == "\n":
            for i, item in enumerate(data):
                for convert in conversions:
                    if (
                        convert["src_start"]
                        <= item
                        < convert["src_start"] + convert["length"]
                    ):
                        data[i] = item + convert["dest_start"] - convert["src_start"]
            conversions = []

        else:
            temp_data = line.split()
            temp_data = [int(x) for x in temp_data]
            dest_start, src_start, length = temp_data
            conversions.append(
                {"dest_start": dest_start, "src_start": src_start, "length": length}
            )

    # Data goes to end of file
    for i, item in enumerate(data):
        for convert in conversions:
            if convert["src_start"] <= item < convert["src_start"] + convert["length"]:
                data[i] = item + convert["dest_start"] - convert["src_start"]

    # print(data)
    print(f"Lowest location: {min(data)}")


def part_2():
    input_file = open("src/day_5/puzzle_input.txt", "r", encoding="utf-8")
    lines = input_file.readlines()
    ranges = []
    conversions = []

    for line in lines:
        if ":" in line:
            if not ranges:
                _, temp_ranges = line.split(": ")
                temp_ranges = temp_ranges.split()
                temp_ranges = [int(x) for x in temp_ranges]
                for i in range(0, len(temp_ranges) - 1, 2):
                    ranges.append(
                        {
                            "start": temp_ranges[i],
                            "end": temp_ranges[i] + temp_ranges[i + 1] - 1,
                        }
                    )
            else:
                conversions.append([])

        elif line != "\n":
            new_conversion = line.split()
            new_conversion = [int(x) for x in new_conversion]
            dest_start, src_start, length = new_conversion
            conversions[-1].append(
                {
                    "src_start": src_start,
                    "src_end": src_start + length - 1,
                    "dest_start": dest_start,
                    "dest_end": dest_start + length - 1,
                }
            )

    for section in conversions:
        section.sort(key=lambda x: x["src_start"])
        ranges.sort(key=lambda x: x["start"])
        start = 0
        stop = len(ranges)
        for convert in section:
            i = start
            # Can't just use len(ranges) here b/c it'll fail when a split happens on the last pass
            while i < stop:
                # Breaking up sections
                # Starts after
                if ranges[i]["start"] > convert["src_end"]:
                    start = i
                    break
                # Starts before, ends in/after
                if (
                    ranges[i]["start"] < convert["src_start"]
                    and ranges[i]["end"] >= convert["src_start"]
                ):
                    first = {
                        "start": ranges[i]["start"],
                        "end": convert["src_start"] - 1,
                    }
                    second = {"start": convert["src_start"], "end": ranges[i]["end"]}

                    ranges[i] = first
                    ranges.insert(i + 1, second)
                    stop += 1
                # Starts in, ends after
                elif (
                    convert["src_start"] <= ranges[i]["start"] <= convert["src_end"]
                    and ranges[i]["end"] > convert["src_end"]
                ):
                    first = {
                        "start": ranges[i]["start"],
                        "end": convert["src_end"],
                    }
                    second = {"start": convert["src_end"] + 1, "end": ranges[i]["end"]}

                    ranges[i] = first
                    ranges.insert(i + 1, second)
                    stop += 1

                # Converting if appropriate
                if (
                    ranges[i]["start"] >= convert["src_start"]
                    and ranges[i]["end"] <= convert["src_end"]
                ):
                    change = convert["dest_start"] - convert["src_start"]
                    ranges[i] = {
                        "start": ranges[i]["start"] + change,
                        "end": ranges[i]["end"] + change,
                    }
                i += 1

            else:
                break

    ranges.sort(key=lambda x: x["start"])
    # print(ranges)
    print(f"Lowest location: {ranges[0]['start']}")


part_2()
