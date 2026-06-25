s = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

pos = 50
print(
    sum(
        (pos := (pos + int(line[1:]) * (1 if line[0] == "R" else -1)) % 100) == 0
        for line in s.splitlines()
    )
)

pos, ans = 50, 0
for m in s.splitlines():
    d = 1 if m[0] == "R" else -1
    n = int(m[1:])
    ans += (n - ((-pos * d) % 100 or 100)) // 100 + 1
    pos = (pos + d * n) % 100
print(ans)
