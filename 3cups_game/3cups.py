# macking the 3 cups  random game

from random import shuffle

cups = [" ", "o", " "]

def shuffleList(alist):
    shuffle(alist)
    return alist
    
def guess_player():
    guessed_index = ""
    while guessed_index not in ['0', '1', "2"]:
        guessed_index = input("please enter 0 or 1 or 2: ")
    return int(guessed_index)
def check_game(alist, index):
    if alist[index] == "o":
        print("You WON!")
    else:
        print("You LOST ")
    print(f"here it is the list {alist}")

# shuffeled_list = shuffleList(cups)
# guessed_input = guess_player()
# check_game(shuffeled_list, guessed_input)
check_game(shuffleList(cups), guess_player())
