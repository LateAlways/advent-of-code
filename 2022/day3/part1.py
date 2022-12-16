data = open("input.txt")

def letter_index(letter):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  return alphabet.index(letter)+1

total = 0

for line in data.readlines():
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    similar = None
    for letter in first:
        if letter in second:
            similar = letter
            break
    index = letter_index(similar.lower())
    if similar == similar.lower():
        total += index
    else:
        total += index+26
print(total)