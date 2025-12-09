from time import time

ranges = [r.split("-") for r in open("day2/day2.in").readlines()[0].split(",")]
repeats = 0

for r in ranges:
    for num in range(int(r[0]), int(r[1])+1):
        l = int(len(str(num))/2)
        if str(num)[:l] == str(num)[l:]:
            repeats += num

print(repeats)


# part 2
for r in ranges:
    for num in range(int(r[0]), int(r[1])+1):
        s = str(num)
        l = len(s)
        for i in range(1, l):
            if not (num in exclude):
                if l%i == 0:
                    splits = []
                    ps = int(l/i)
                    if ps != 1:
                        phantom = s
                        for x in range(ps):
                            split = phantom[:i]
                            splits.append(split)
                            phantom = phantom[i:]
                    if len(set(splits)) == 1: 
                        repeats += num
                        break

print(repeats)

