# Day 6

import re
import numpy as np


def part_1():
    input_file = open("src/day_6/puzzle_input.txt", "r", encoding="utf-8")
    times, records = input_file.readlines()
    times = re.sub("\n", "", times)
    times = re.split(" +", times)
    del times[0]
    times = [int(x) for x in times]
    records = re.split(" +", records)
    del records[0]
    records = [int(x) for x in records]
    winners = []

    for i, time in enumerate(times):
        held = 1  # In ms
        # Distance = time held * (total time - time held)
        while held * (time - held) <= records[i]:
            held += 1
        # Num possibilties = max time - time held - (time held - 1), b/c graph is bell curve
        winners.append(time - held * 2 + 1)

    # print(winners)
    print(f"Lowest location: {np.prod(winners)}")


part_1()
