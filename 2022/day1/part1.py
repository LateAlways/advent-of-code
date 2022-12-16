data = open("input.txt")


elfs = [0]
current = 0
best = -1
for line in data.readlines():
    if line != "\n":
        elfs[current] += int(line.replace("\n",""))
    else:
        if best == -1 or elfs[current] > best:
            best = elfs[current]
        elfs.append(0)
        current += 1
        continue
        
print(best)