from itertools import product

s = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

s = list(map(list, s.splitlines()))

m, n, total = len(s), len(s[0]), 0
for x in range(m):
    for y in range(n):
        total += s[x][y] == "@" and (
            sum(
                s[i][j] == "@"
                for (i, j) in product(range(x - 1, x + 2), range(y - 1, y + 2))
                if 0 <= i < m and 0 <= j < n
            )
            < 5
        )

print(total)

g = [list(row) for row in s.splitlines()]
m, n = len(g), len(g[0])
dirs = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]
total = 0

while True:
    rem = [
        (r, c)
        for r in range(m)
        for c in range(n)
        if g[r][c] == "@"
        and sum(
            0 <= r + dr < m and 0 <= c + dc < n and g[r + dr][c + dc] == "@"
            for dr, dc in dirs
        )
        < 4
    ]

    if not rem:
        break

    total += len(rem)

    for r, c in rem:
        g[r][c] = "."
print(total)
