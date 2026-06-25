from functools import cache

s = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".splitlines()

# beams, w, splits = {s[0].find("S")}, len(s[0]), 0

# for line in s:
#     for b in beams.copy():
#         if line[b] == "^":
#             splits += 1
#             beams.remove(b)
#             if b >= 1:
#                 beams.add(b - 1)
#             if b + 1 <= w:
#                 beams.add(b + 1)

# print(splits)
#

h, w = len(s), len(s[0])


@cache
def count_routes(row, i) -> int:
    if row + 1 == h:
        return 1
    if s[row][i] == "^":
        return (count_routes(row, i - 1) if i >= 1 else 0) + (
            count_routes(row, i + 1) if i + 1 <= w else 0
        )
    else:
        return count_routes(row + 1, i)


print(count_routes(1, s[0].find("S")))
