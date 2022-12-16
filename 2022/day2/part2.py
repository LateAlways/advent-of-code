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

def get_action(action_a, action_b):
    opponent_choice = action_a.replace("\n","").replace("A", "1").replace("B", "2").replace("C","3")
    my_choice = action_b.replace("\n","").replace("X", "1").replace("Y", "2").replace("Z","3")

    #1 = lose
    #2 = draw
    #3 = win

    #1 = rock
    #2 = paper
    #3 = scissors

    choice = 0
    if my_choice == "2":
        choice = opponent_choice
    elif my_choice == "1":
        if opponent_choice == "1":
            choice = "3"
        elif opponent_choice == "2":
            choice = "1"
        elif opponent_choice == "3":
            choice = "2"
    elif my_choice == "3":
        if opponent_choice == "1":
            choice = "2"
        elif opponent_choice == "2":
            choice = "3"
        elif opponent_choice == "3":
            choice = "1"
    return choice

my_score = 0
opponent_score = 0
for line in data.readlines():
    action = get_action(line.split(" ")[0],line.split(" ")[1])
    score = get_score(line.split(" ")[0] + " "+action)
    opponent_score += score[0]
    my_score += score[1]

print(my_score)
print(opponent_score)