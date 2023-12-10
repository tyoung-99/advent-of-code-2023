# Day 2

def part_1():
    MAX = {"red": 12, "green": 13, "blue": 14}

    input_file = open("src/day_2/puzzle_input.txt", "r", encoding="utf-8")
    total_games = input_file.readlines()
    possible_games = []

    for game in total_games:
        id_num, results = game.split(":")
        _ , id_num = id_num.split()

        most_drawn = {"red": 0, "green": 0, "blue": 0}
        for draw in results.split(";"):
            for cubes in draw.split(","):
                num, color = cubes.split()
                if int(num) > most_drawn[color]:
                    most_drawn[color] = int(num)

        legal = True
        for color, count in most_drawn.items():
            if count > MAX[color]:
                legal = False

        if legal:
            possible_games.append(int(id_num))

    # print(possible_games)
    print(f"Sum of IDs of possible games: {sum(possible_games)}")

def part_2():
    input_file = open("src/day_2/puzzle_input.txt", "r", encoding="utf-8")
    total_games = input_file.readlines()
    powers = []

    for game in total_games:
        _, results = game.split(":")

        most_drawn = {"red": 0, "green": 0, "blue": 0}
        for draw in results.split(";"):
            for cubes in draw.split(","):
                num, color = cubes.split()
                if int(num) > most_drawn[color]:
                    most_drawn[color] = int(num)

        power = 1
        for _, count in most_drawn.items():
            power *= count
        powers.append(power)

    # print(powers)
    print(f"Sum of powers of all games: {sum(powers)}")

part_2()
