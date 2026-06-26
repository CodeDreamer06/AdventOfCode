from collections import defaultdict

s = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

red = [tuple(map(int, line.split(","))) for line in s.splitlines()]
n = len(red)


def make_segs(vals):
    vals = sorted(set(vals))
    segs, idx = [], {}
    for i, x in enumerate(vals):
        idx[x] = len(segs)
        segs.append((x, x))
        if i + 1 < len(vals) and x + 1 <= vals[i + 1] - 1:
            segs.append((x + 1, vals[i + 1] - 1))
    return segs, idx


xs, xid = make_segs(x for x, y in red)
ys, yid = make_segs(y for x, y in red)

vert = []
horiz = defaultdict(list)

for a, b in zip(red, red[1:] + red[:1]):
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        vert.append((x1, min(y1, y2), max(y1, y2)))
    else:
        horiz[y1].append((min(x1, x2), max(x1, x2)))

bad = []

for ylo, yhi in ys:
    y = ylo
    cross = sorted(x for x, a, b in vert if a < y <= b)

    intervals = [(cross[i], cross[i + 1]) for i in range(0, len(cross), 2)]
    intervals += horiz[y]

    intervals.sort()
    merged = []
    for a, b in intervals:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    row = [1] * len(xs)  # 1 = outside, 0 = inside/on polygon
    p = 0
    for a, b in merged:
        while p < len(xs) and xs[p][1] < a:
            p += 1
        while p < len(xs) and xs[p][0] <= b:
            row[p] = 0
            p += 1

    bad.append(row)

# 2D prefix sum of outside blocks
pref = [[0] * (len(xs) + 1)]
for row in bad:
    cur = [0]
    run = 0
    prev = pref[-1]
    for i, v in enumerate(row, 1):
        run += v
        cur.append(prev[i] + run)
    pref.append(cur)


def clear(x1, x2, y1, y2):
    xa, xb = xid[x1], xid[x2]
    ya, yb = yid[y1], yid[y2]
    return (
        pref[yb + 1][xb + 1] - pref[ya][xb + 1] - pref[yb + 1][xa] + pref[ya][xa]
    ) == 0


p1 = p2 = 0

for i, (x1, y1) in enumerate(red):
    for x2, y2 in red[i + 1 :]:
        xlo, xhi = sorted((x1, x2))
        ylo, yhi = sorted((y1, y2))
        area = (xhi - xlo + 1) * (yhi - ylo + 1)

        p1 = max(p1, area)

        if area > p2 and clear(xlo, xhi, ylo, yhi):
            p2 = area

print(p1)
print(p2)
