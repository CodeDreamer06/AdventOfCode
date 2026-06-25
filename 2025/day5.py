raw_fresh = sorted(
    """3-5
10-14
16-20
12-18""".splitlines(),
    key=lambda l: int(l[: l.find("-")]),
)

fresh = []
for f in raw_fresh:
    f = list(map(int, f.split("-")))
    if not fresh or fresh[-1][1] < f[0]:
        fresh.append(f)
    else:
        fresh[-1][1] = max(fresh[-1][1], f[1])

available = map(
    int,
    """1
5
8
11
17
32""".splitlines(),
)

print(sum(start <= item_id <= end for item_id in available for start, end in fresh))
print(sum(end - start + 1 for start, end in fresh))
