# Day 1

import re


def part_1():
    input_file = open("src/day_1/calibration_doc.txt", "r", encoding="utf-8")
    vals = input_file.readlines()

    for i, val in enumerate(vals):
        digits = None
        last_digit = 0
        for char in val:
            if char.isnumeric():
                if digits is None:
                    digits = int(char) * 10
                last_digit = int(char)
        digits += last_digit
        vals[i] = digits

    print(f"Sum of calibration values: {sum(vals)}")


def part_2():
    digit_words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    input_file = open("src/day_1/calibration_doc.txt", "r", encoding="utf-8")

    vals = input_file.readlines()
    for i, val in enumerate(vals):
        # Preserve 1st/last letter in swap b/c those might be part of other words
        for digit, word in enumerate(digit_words):
            val = val.replace(
                word, word[0:1] + str(digit) + word[len(word) - 1 : len(word)]
            )

        val = re.sub("[^0-9]", "", val)
        vals[i] = int(val[0]) * 10 + int(val[len(val) - 1])

    print(f"Sum of calibration values: {sum(vals)}")


part_2()
