s = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

ans = 0
for r in s.split(","):
    start, end = r.split("-")
    for i in range(int(start), int(end) + 1):
        if (l := len(st := str(i))) % 2 == 0 and st[: l // 2] == st[l // 2 :]:
            ans += i
print(ans)

ans = 0
for r in s.split(","):
    start, end = r.split("-")
    for i in range(int(start), int(end) + 1):
        if (st := str(i)) in (st * 2)[1:-1]:
            ans += i
print(ans)
