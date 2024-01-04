# Day 17

from heapq import heappush, heappop


def part_1(puzzle):
    def update_node(new_node, current):
        new_x, new_y = new_node
        if not (0 <= new_x < len(city[0]) and 0 <= new_y < len(city)):
            return

        coord_difference = (new_x - current[0], new_y - current[1])
        node_a = current
        for _ in range(3):
            node_b = heat_losses[node_a]["prev_node"]
            if node_b is None:
                break
            prev_difference = (node_a[0] - node_b[0], node_a[1] - node_b[1])
            if prev_difference != coord_difference:
                break
            node_a = node_b
        else:
            return

        new_heat_loss = (
            int(city[new_node[1]][new_node[0]]) + heat_losses[current]["least_loss"]
        )
        if new_heat_loss < heat_losses[new_node]["least_loss"]:
            heat_losses[new_node] = {
                "least_loss": new_heat_loss,
                "prev_node": current,
            }

        print(end="")

    city = [line.strip() for line in puzzle]
    dest = (len(city[0]) - 1, len(city) - 1)

    heat_losses = {}
    unvisited = [(x, y) for y, row in enumerate(city) for x, _ in enumerate(row)]
    for node in unvisited:
        heat_losses[node] = {"least_loss": float("inf"), "prev_node": None}
    heat_losses[(0, 0)] = {"least_loss": 0, "prev_node": None}

    while dest in unvisited:
        current = min(unvisited, key=lambda node: heat_losses[node]["least_loss"])
        unvisited.remove(current)

        for x_change, y_change in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            calc_node = (current[0] + x_change, current[1] + y_change)
            if calc_node in unvisited:
                update_node(calc_node, current)

    solution = [["." for x in city[0]] for y in city]
    solution[0][0] = "#"

    trace = dest
    while trace != (0, 0):
        solution[trace[1]][trace[0]] = "#"
        trace = heat_losses[trace]["prev_node"]

    for row in solution:
        print("".join(str(char) for char in row))
    print()

    print(f"Least heat loss: {heat_losses[dest]['least_loss']}")


def part_2(puzzle):
    grid = [list(map(int, line.strip())) for line in puzzle]

    seen = set()
    queue = [(0, 0, 0, 0, 0, 0)]

    while queue:
        heat_loss, row, col, row_change, col_change, consecutive_steps = heappop(queue)

        if consecutive_steps >= 4 and (row, col) == (len(grid) - 1, len(grid[0]) - 1):
            print(f"Least heat loss: {heat_loss}")
            break

        if (row, col, row_change, col_change, consecutive_steps) in seen:
            continue

        seen.add((row, col, row_change, col_change, consecutive_steps))

        if consecutive_steps < 10 and (row_change, col_change) != (0, 0):
            next_row = row + row_change
            next_col = col + col_change
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                heappush(
                    queue,
                    (
                        heat_loss + grid[next_row][next_col],
                        next_row,
                        next_col,
                        row_change,
                        col_change,
                        consecutive_steps + 1,
                    ),
                )

        if consecutive_steps >= 4 or (row_change, col_change) == (0, 0):
            for turn_row_change, turn_col_change in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (turn_row_change, turn_col_change) != (row_change, col_change) and (
                    turn_row_change,
                    turn_col_change,
                ) != (-row_change, -col_change):
                    next_row = row + turn_row_change
                    next_col = col + turn_col_change
                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                        heappush(
                            queue,
                            (
                                heat_loss + grid[next_row][next_col],
                                next_row,
                                next_col,
                                turn_row_change,
                                turn_col_change,
                                1,
                            ),
                        )


with open("src/day_17/puzzle_input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readlines()
part_2(puzzle)
