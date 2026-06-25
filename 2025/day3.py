banks = """987654321111111
811111111111119
234234234234278
818181911112111"""

s, k = 0, 2
for b in banks.splitlines():
    stack, remainder = [], len(b)
    for digit in b:
        while stack and stack[-1] < digit and (len(stack) + remainder > k):
            stack.pop()

        if len(stack) < k:
            stack.append(digit)

        remainder -= 1

    s += int("".join(stack))
print(s)
