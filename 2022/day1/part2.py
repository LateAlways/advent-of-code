data = open("input.txt")


elfs = [0]
current = 0
for line in data.readlines():
    if line != "\n":
        elfs[current] += int(line.replace("\n",""))
    else:
        elfs.append(0)
        current += 1
        continue
        
total = 0
for calories in sorted(elfs)[-3:]:
    total += calories
print(total)