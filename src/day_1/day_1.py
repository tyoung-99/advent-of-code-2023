# Day 1

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
