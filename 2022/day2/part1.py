data = open("input.txt")

def get_score(line):
    opponent_choice = line.split(" ")[0].replace("\n","").replace("A", "1").replace("B", "2").replace("C","3")
    my_choice = line.split(" ")[1].replace("\n","").replace("X", "1").replace("Y", "2").replace("Z","3")

    #1 = Rock
    #2 = Paper
    #3 = Scissors

    score = []
    if opponent_choice == my_choice:
        score = [int(opponent_choice)+3, int(my_choice)+3]
    elif opponent_choice == "1" and my_choice == "2":
        score = [int(opponent_choice), int(my_choice)+6]
    elif opponent_choice == "1" and my_choice == "3":
        score = [int(opponent_choice)+6, int(my_choice)]
    elif opponent_choice == "2" and my_choice == "1":
        score = [int(opponent_choice)+6, int(my_choice)]
    elif opponent_choice == "2" and my_choice == "3":
        score = [int(opponent_choice), int(my_choice)+6]
    elif opponent_choice == "3" and my_choice == "1":
        score = [int(opponent_choice), int(my_choice)+6]
    elif opponent_choice == "3" and my_choice == "2":
        score = [int(opponent_choice)+6, int(my_choice)]

    return score

my_score = 0
opponent_score = 0
for line in data.readlines():
    score = get_score(line)
    opponent_score += score[0]
    my_score += score[1]

print(my_score)
print(opponent_score)