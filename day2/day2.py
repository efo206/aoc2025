ranges = [r.split("-") for r in open("day2/day2.in").readlines()[0].split(",")]
repeats = 0

for r in ranges:
    for num in range(int(r[0]), int(r[1])+1):
        l = int(len(str(num))/2)
        if str(num)[:l] == str(num)[l:]:
            repeats += num

print(repeats)
