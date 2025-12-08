inp = open("day2/day2.in").readlines()[0].split(",")
ranges = []
for r in inp: ranges.append(r.split("-"))
repeats = 0

for r in ranges:
    for num in range(int(r[0]), int(r[1])+1):
        n = str(num)
        l = int(len(n)/2)
        if n[:l] == n[l:]:
            repeats += num

print(repeats)
