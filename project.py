# this is a tic tac toe project using python
from random import randint
import os
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
valid_input = ['',1,2,3,4,5,6,7,8,9] # the cells enumeration numbers
player1_info = ['', '']
player2_info = ['', '']
count = 0 # count eq to 9 means no one wins
player_turn = 0
playing = True
def init():
    global count, player_turn, playing, board, valid_input, player1_info, player2_info
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    valid_input = ['',1,2,3,4,5,6,7,8,9] # the cells enumeration numbers
    player1_info = ['', '']
    player2_info = ['', '']
    count = 0
    player_turn = 0
    playing = True



def display(l, r):
    line1 = '-------------               -------------'
    line2 = f'| {l[1]} | {l[2]} | {l[3]} |               | {r[1]} | {r[2]} | {r[3]} |'
    line3 = '-------------               -------------'
    line4 = f'| {l[4]} | {l[5]} | {l[6]} |               | {r[4]} | {r[5]} | {r[6]} |'
    line5 = '-------------               -------------'
    line6 = f'| {l[7]} | {l[8]} | {l[9]} |               | {r[7]} | {r[8]} | {r[9]} |'
    line7 = '-------------               -------------'
    print("\n"* 8)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)




def set_playersInfo():
    player1_info[0] = input("Enter the name of Player 1: ")
    while True:
        player1_info[1] = input("Please choose either X or O: ")
        if player1_info[1] in ['X', 'x', 'O', 'o']:
            player1_info[1] = player1_info[1].upper()
            break
    player2_info[0] = input("Enter the name of the player 2: ")
    if player1_info[1] == 'O':
        player2_info[1] = 'X'
    else:
        player2_info[1] = 'O'



def player_input():
    global count
    count += 1 
    if player_turn == 1 :
        print(f"the turn of Player1: {player1_info[0]}")
    else:
        print(f"the turn of Player2: {player2_info[0]}")

    while True:
        try:
            result = int(input("Please choose a cell from displaying board: "))
        except:
            print("Invalid input, please do not input a string, try again")
        else:
            if result in valid_input:
                valid_input[result] = " "
                return result
            else:
                print("Invalid input, ALREADY CHOOSED, please select a cell from the displaying board")

def set_board(index, player_turn, board):
    if player_turn == 1:
        board[index] = player1_info[1]
    else:
        board[index] = player2_info[1]
        
    return board
def switch_turn(turn):
    if turn == 1:
        return 2
    else: 
        return 1
def check_winner(board):
  if board[1] == board[2] == board[3] != ' ':
    return True
  elif board[4] == board[5] == board[6] != ' ':
    return True
  elif board[7] == board[8] == board[9] != ' ':
    return True
  elif board[1] == board[4] == board[7] != ' ':
    return True
  elif board[2] == board[5] == board[8] != ' ':
    return True
  elif board[3] == board[6] == board[9] != ' ':
    return True
  elif board[1] == board[5] == board[9] != ' ':
    return True
  elif board[3] == board[5] == board[7] != ' ':
    return True
  else:
    return False




script_path = './banner.sh'


# Run the Bash script

os.system(f'bash {script_path}')


while playing:
    init()
    set_playersInfo()
    player_turn = randint(1, 2)
    display(board, valid_input)
    while True:
      index = player_input()
      board = set_board(index, player_turn, board)
      display(board, valid_input)
      if check_winner(board):
         if player_turn == 1:
            print(f"Congratulations Player1 {player1_info[0]} You WON!!!! ")
            print("exiting form first while")
            break
         else:
            print(f"Congratulations Player2 {player2_info[0]} You WON!!!! ")
            print("exiting form first while")
            break
      elif count >= 9:
         print("It's a TIE No one WON")
         break
      player_turn = switch_turn(player_turn)

      # asking the useers it they cant to continue playing
    while True:
       user_input = input("Do you want to play another game Y/N?")
       if user_input in ['Y', 'y']:
          print("OKEY let's Play again shall we ?")
          break
       elif user_input in ['N', 'n']:
          playing = False
          print("Okey Exiting from the game Now")
          break

