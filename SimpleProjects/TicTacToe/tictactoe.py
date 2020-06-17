import os


clear = lambda: os.system('cls')

clear()

print(" 7 | 8 | 9 ")
print(" 4 | 5 | 6 ")
print(" 1 | 2 | 3 ")

new_game_list = ['_','_','_']
row1 = new_game_list.copy()
row2 = new_game_list.copy()
row3 = new_game_list.copy()

complete_check = 'no'
picked_dict = {1: False,
               2: False,
               3: False,
               4: False,
               5: False,
               6: False,
               7: False,
               8: False,
               9: False}

def new_board():
    """Create a new board if playing again"""
    for x in range(len(row1)):
        row1[x] = '_'
    for x in range(len(row2)):
        row2[x] = '_'
    for x in range(len(row3)):
        row3[x] = '_'

    clear()

    print(" 7 | 8 | 9 ")
    print(" 4 | 5 | 6 ")
    print(" 1 | 2 | 3 ")

def row_getter(value):
    switcher = {
        1: row1,
        2: row2,
        3: row3
    }
    return switcher.get(value, "Invalid entry")


def move_made():
    """ Clear the screen and update the tic tac toe bord to reflect the move """
    clear()

    print(" " + str(row1[0]) + " | " + str(row1[1]) + " | " + str(row1[2]) + " ")
    print(" " + str(row2[0]) + " | " + str(row2[1]) + " | " + str(row2[2]) + " ")
    print(" " + str(row3[0]) + " | " + str(row3[1]) + " | " + str(row3[2]) + " ")

def ai_move_made():
    """Ai Move choices"""
    # search for ai piece
    ai_pawn = 'O'

    # Make backup of board
    board_copy = {1: row3[0],
             2: row3[1],
             3: row3[2],
             4: row2[0],
             5: row2[1],
             6: row2[2],
             7: row1[0],
             8: row1[1],
             9: row1[2]}

    for x in range(1,len(board_copy)):
        print(board_copy[x])

def make_move(player):
    """For two human controled players, asled user for input and places piece on board."""
    while True:
        # This worked but can be simplified for the end user.
        # location = tuple(int(x.strip()) for x in input('Enter the location x , y for your piece ').split(','))
        # location_x, location_y = location
        if player == 0:
            location = int(input('X, Enter the location for your piece: '))
        else:
            location = int(input('O, Enter the location for your piece: '))
        print(location)
        # if (location_y - 1 < 0 and location_y - 1 > 2) and (location_x - 1 < 0 and location_x - 1 > 2):
        if 1 > location > 9:
            print('Please enter the correct location ')
            continue
        elif picked_dict[location] is True:
            print('Please enter a location that has not been chosen. ')
        else:
            picked_dict[location] = True
            if location == 1:
                if player == 0:
                    row3[0] = 'X'
                else:
                    row3[0] = 'O'
            elif location == 2:
                if player == 0:
                    row3[1] = 'X'
                else:
                    row3[1] = 'O'
            elif location == 3:
                if player == 0:
                    row3[2] = 'X'
                else:
                    row3[2] = 'O'
            elif location == 4:
                if player == 0:
                    row2[0] = 'X'
                else:
                    row2[0] = 'O'
            elif location == 5:
                if player == 0:
                    row2[1] = 'X'
                else:
                    row2[1] = 'O'
            elif location == 6:
                if player == 0:
                    row2[2] = 'X'
                else:
                    row2[2] = 'O'
            elif location == 7:
                if player == 0:
                    row1[0] = 'X'
                else:
                    row1[0] = 'O'
            elif location == 8:
                if player == 0:
                    row1[1] = 'X'
                else:
                    row1[1] = 'O'
            elif location == 9:
                if player == 0:
                    row1[2] = 'X'
                else:
                    row1[2] = 'O'
            move_made()
            break


def win_check(player, round):

    # There was a simpler way to write this, if the last checked value is equal to each other but not _ it is given that we do not need to check the rest for the _
    # row1[0] == row2[1] == row3[2] and  row1[0] != '_' and row2[1] != '_' and row3[2] != '_': can be simplified as row1[0] == row2[1] == row3[2] != '_': 
    if round == 9:
        print("tie")
    elif row1[0] == row2[1] == row3[2] != '_':
        return 'winner'
        # break
    elif row3[0] == row2[1] == row1[2] != '_':
        return 'winner'
        # break
    elif row1[0] == row1[1] == row1[2] != '_':
        return 'winner'
        # break
    elif row2[0] == row2[1] == row2[2] != '_':
        return 'winner'
        # break
    elif row3[0] == row3[1] == row3[2] != '_':
        return 'winner'
        # break
    elif row3[0] == row2[0] == row1[0] != '_':
        return 'winner'
        # break
    elif row3[2] == row2[2] == row1[2] != '_':
        return 'winner'
        # break
    elif row3[1] == row2[1] == row1[1] != '_':
        return 'winner'
        # break
    else:
        make_move(player)

# win_check()
def game_loop():
    while True:
        for x in range(0,10):
            if(x % 2 == 0):
                complete_check = win_check(0,x)
                if complete_check == 'winner':
                    print('O has won!')
                    ai_move_made()
                    break
            else:
                complete_check = win_check(1,x)
                if complete_check == 'winner':
                    print('X has won!')
                    break
        
        if input('Enter y to replay: ').lower() != 'y':
            break
        else:
            new_board()

game_loop()

