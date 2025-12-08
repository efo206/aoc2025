inp = open("day1.in").readlines()
# cleanup
for i, line in enumerate(inp):
    inp[i] = line[:-1]
    if inp[i][0] == "R":
        inp[i] = inp[i][1:]
    else:
        inp[i] = f"-{inp[i][1:]}"

for i, _ in enumerate(inp):
    inp[i] = int(inp[i])

dial = 50
zero_count = 0

for i in inp:
    if i >= 0:
        if i > 99: i %= 100
        dial += i
    else:
        i = abs(i)
        if i > 99: i %= 100
        dial = 100 - i + dial
    if dial > 99: dial %= 100
    if dial == 0: zero_count += 1
print(zero_count)