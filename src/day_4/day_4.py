# Day 4

import re

def part_1():
    input_file = open("src/day_4/puzzle_input.txt", "r", encoding="utf-8")
    cards = input_file.readlines()
    card_points = []

    for card in cards:
        _, card = re.split(": +", card)
        winning_nums, our_nums = re.split(r" \| +", card)
        winning_nums = winning_nums.split()
        our_nums = our_nums.split()

        points = 0
        for check in our_nums:
            if check in winning_nums:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        card_points.append(points)

    # print(card_points)
    print(f"Sum of point values: {sum(card_points)}")

part_1()
