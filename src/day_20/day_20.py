# Day 20

from enum import Enum


def part_1(puzzle):
    def get_modules(puzzle):
        modules = {}
        for line in puzzle:
            name, line = line.split(" -> ")
            module_type = name[0]
            if module_type in ("%", "&"):
                name = name[1:]
            dests = line.strip().split(", ")

            modules[name] = {
                "name": name,
                "type": module_type,
                "dests": dests,
                "on_state": False,
                "memory": {},
            }

        for module_1 in modules.values():
            if module_1["type"] != "&":
                continue
            for module_2 in modules.values():
                if module_1["name"] in module_2["dests"]:
                    module_1["memory"][module_2["name"]] = Pulse.LOW

        return modules

    def push_button(modules):
        queue = [["broadcaster", Pulse.LOW, None]]
        low_count, high_count = 0, 0
        while queue:
            mod_to_name, pulse, mod_from = queue.pop(0)
            next_pulse = pulse

            if pulse == Pulse.HIGH:
                high_count += 1
            else:
                low_count += 1

            if mod_to_name not in modules.keys():
                continue

            mod_to = modules[mod_to_name]
            match mod_to["type"]:
                case "%":
                    if pulse == Pulse.HIGH:
                        continue
                    mod_to["on_state"] = not mod_to["on_state"]
                    next_pulse = Pulse.LOW
                    if mod_to["on_state"]:
                        next_pulse = Pulse.HIGH

                case "&":
                    mod_to["memory"][mod_from] = pulse
                    next_pulse = Pulse.LOW
                    if any(
                        mem_pulse == Pulse.LOW
                        for mem_pulse in mod_to["memory"].values()
                    ):
                        next_pulse = Pulse.HIGH

            for next_mod in mod_to["dests"]:
                queue.append([next_mod, next_pulse, mod_to["name"]])

        return low_count, high_count

    Pulse = Enum("Pulse", ["HIGH", "LOW"])
    modules = get_modules(puzzle)
    low_count, high_count = 0, 0
    for _ in range(1000):
        new_low, new_high = push_button(modules)
        low_count += new_low
        high_count += new_high
    # print(low_count, high_count)
    print(f"Product of low/high pulses: {low_count * high_count}")


with open("src/day_20/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_1(puzzle)
