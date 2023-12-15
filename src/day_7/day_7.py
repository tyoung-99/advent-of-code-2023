# Day 7

import functools


def part_1():
    def get_type(hand):
        uniques = list(set(hand))
        match len(uniques):
            case 1:  # 5 of a kind
                hand_type = 6
            case 2:
                # 4 of a kind
                if hand.count(uniques[0]) == 4 or hand.count(uniques[0]) == 1:
                    hand_type = 5
                # Full house
                else:
                    hand_type = 4
            case 3:
                # 2 pair
                if hand.count(uniques[0]) == 2 or hand.count(uniques[1]) == 2:
                    hand_type = 2
                # 3 of a kind
                else:
                    hand_type = 3
            case 4:  # 1 pair
                hand_type = 1
            case 5:  # High card
                hand_type = 0
        return hand_type

    def sort_hands(first, second):
        SUIT_KEY = {"T": 0, "J": 1, "Q": 2, "K": 3, "A": 4}

        if first["type"] > second["type"]:
            return 1
        if first["type"] < second["type"]:
            return -1

        for i, char in enumerate(first["cards"]):
            if not char.isnumeric():
                if second["cards"][i].isnumeric():
                    return 1
                compare = SUIT_KEY[char] - SUIT_KEY[second["cards"][i]]
                if compare != 0:
                    return compare

            elif not second["cards"][i].isnumeric():
                return -1

            else:
                compare = int(char) - int(second["cards"][i])
                if compare != 0:
                    return compare

        return 0

    input_file = open("src/day_7/puzzle_input.txt", "r", encoding="utf-8")
    data = input_file.readlines()
    hands = []

    for line in data:
        cards, bid = line.split()
        hands.append({"cards": cards, "bid": int(bid), "type": get_type(cards)})

    hands = sorted(hands, key=functools.cmp_to_key(sort_hands))

    # print(hands)
    print(
        f"Total winnings: {sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands))}"
    )


def part_2():
    def get_type(hand):
        uniques = set(hand)
        if len(uniques) > 1:
            uniques.discard("J")
            mimic = max(uniques, key=hand.count)
            hand = hand.replace("J", mimic)
        uniques = list(uniques)

        match len(uniques):
            case 1:  # 5 of a kind
                hand_type = 6
            case 2:
                # 4 of a kind
                if hand.count(uniques[0]) == 4 or hand.count(uniques[0]) == 1:
                    hand_type = 5
                # Full house
                else:
                    hand_type = 4
            case 3:
                # 2 pair
                if hand.count(uniques[0]) == 2 or hand.count(uniques[1]) == 2:
                    hand_type = 2
                # 3 of a kind
                else:
                    hand_type = 3
            case 4:  # 1 pair
                hand_type = 1
            case 5:  # High card
                hand_type = 0
        return hand_type

    def sort_hands(first, second):
        KEY = {
            "J": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 6,
            "8": 7,
            "9": 8,
            "T": 9,
            "Q": 10,
            "K": 11,
            "A": 12,
        }

        if first["type"] > second["type"]:
            return 1
        if first["type"] < second["type"]:
            return -1

        for i, char in enumerate(first["cards"]):
            compare = KEY[char] - KEY[second["cards"][i]]
            if compare != 0:
                return compare

        return 0

    input_file = open("src/day_7/puzzle_input.txt", "r", encoding="utf-8")
    data = input_file.readlines()
    hands = []

    for line in data:
        cards, bid = line.split()
        hands.append({"cards": cards, "bid": int(bid), "type": get_type(cards)})

    hands = sorted(hands, key=functools.cmp_to_key(sort_hands))

    # print(hands)
    print(
        f"Total winnings: {sum(hand['bid'] * (i + 1) for i, hand in enumerate(hands))}"
    )


part_2()
