s = "121212"
l = len(s)

splits= []

# i is possible split length
# ps is possible amount of splits with that split length
for i in range(1, l):
    if l%i == 0:
        ps = int(l/i)
        if ps != 1:
            phantom = s
            for x in range(ps):
                split = phantom[:i]
                splits.append(split)
                phantom = phantom[i:]
            print(ps)
            print(i)
        if len(set(splits)) == 1: print(splits)
        splits = []