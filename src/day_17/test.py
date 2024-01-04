from heapq import heappush, heappop


def part_1(puzzle):
    grid = [list(map(int, line.strip())) for line in puzzle]

    seen = set()
    queue = [(0, 0, 0, 0, 0, 0)]

    while queue:
        heat_loss, row, col, row_change, col_change, consecutive_steps = heappop(queue)

        if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
            print(f"Least heat loss: {heat_loss}")
            break

        if (row, col, row_change, col_change, consecutive_steps) in seen:
            continue

        seen.add((row, col, row_change, col_change, consecutive_steps))

        if consecutive_steps < 3 and (row_change, col_change) != (0, 0):
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
part_1(puzzle)
