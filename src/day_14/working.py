# From u/lscddit on Reddit

import numpy as np

m = np.genfromtxt(
    "src/day_14/puzzle_input.txt", dtype=bytes, comments=None, delimiter=1
).astype(str)


def show(m):
    print(np.sum(m == "O", axis=1) @ np.arange(m.shape[0], 0, -1))


def tilt(m):
    for offset in range(1, m.shape[0]):
        for row in range(m.shape[0] - offset):
            selection = (m[row, :] == ".") & (m[row + 1, :] == "O")
            m[row, selection] = "O"
            m[row + 1, selection] = "."


cycles, lookup, found, i = 1000000000 * 4, {}, False, 0
while i < cycles:
    tilt(np.rot90(m, (4 - i) % 4))
    if i == 0:
        show(m)
    if found == False:
        check = hash(m.data.tobytes())
        if check in lookup:
            found = True
            print(f"cycles: {cycles}, i: {i}, lookup[check]: {lookup[check]}, ")
            i = cycles - (cycles - i) % (i - lookup[check])
            print(i)
        else:
            lookup[check] = i
    i += 1
show(m)
