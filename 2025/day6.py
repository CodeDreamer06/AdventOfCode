from math import prod

s = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +"""

# rows = s.splitlines()
# w = max(map(len, rows))
# rows = [r.ljust(w) for r in rows]
# used = [any(r[c] != " " for r in rows) for c in range(w)]

# total = c = 0

# while c < w:
#     if not used[c]:
#         c += 1
#         continue

#     start = c
#     while c < w and used[c]:
#         c += 1

#     block = ["".join(r[start:c]).strip() for r in rows]
#     op = block[-1]
#     nums = list(map(int, filter(None, block[:-1])))

#     total += sum(nums) if op == "+" else prod(nums)

# print(total)

a = s.splitlines()
w = max(map(len, a))
a = [s.ljust(w) for s in a]

used = [any(r[c] != " " for r in a) for c in range(w)]

ans = 0
c = 0

while c < w:
    if not used[c]:
        c += 1
        continue

    l = c
    while c < w and used[c]:
        c += 1
    r = c

    op = next(x for x in a[-1][l:r] if x != " ")

    nums = [
        int("".join(a[y][x] for y in range(len(a) - 1) if a[y][x] != " "))
        for x in range(r - 1, l - 1, -1)
    ]

    ans += sum(nums) if op == "+" else prod(nums)

print(ans)
