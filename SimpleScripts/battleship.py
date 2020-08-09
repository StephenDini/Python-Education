import random as R
import pprint as pp
from os import system, name

# Fog of war revealed
BOARD = ["-","-","-","-","-","-","-","-","-","-", #  0- 9
         "-","-","-","-","-","-","-","-","-","-", # 10-19
         "-","-","-","-","-","-","-","-","-","-", # 20-29
         "-","-","-","-","-","-","-","-","-","-", # 30-39
         "-","-","-","-","-","-","-","-","-","-", # 40-49
         "-","-","-","-","-","-","-","-","-","-", # 50-59
         "-","-","-","-","-","-","-","-","-","-", # 60-69
         "-","-","-","-","-","-","-","-","-","-", # 70-79
         "-","-","-","-","-","-","-","-","-","-", # 80-89
         "-","-","-","-","-","-","-","-","-","-"] # 90-99


# What the player will see
OBSCURD_BOARD = ["X","X","X","X","X","X","X","X","X","X", #  0X 9
                 "X","X","X","X","X","X","X","X","X","X", # 10X19
                 "X","X","X","X","X","X","X","X","X","X", # 20X29
                 "X","X","X","X","X","X","X","X","X","X", # 30X39
                 "X","X","X","X","X","X","X","X","X","X", # 40X49
                 "X","X","X","X","X","X","X","X","X","X", # 50X59
                 "X","X","X","X","X","X","X","X","X","X", # 60X69
                 "X","X","X","X","X","X","X","X","X","X", # 70X79
                 "X","X","X","X","X","X","X","X","X","X", # 80X89
                 "X","X","X","X","X","X","X","X","X","X"] # 90-99

# Ship size enums
TINY_SHIP = 'TT'
SMALL_SHIP = 'SSS'
MEDIUM_SHIP = "MMMM"
LARGE_SHIP = "LLLLL"
DEBUG = False

gamemode = [TINY_SHIP, MEDIUM_SHIP, MEDIUM_SHIP, LARGE_SHIP, LARGE_SHIP]

def place_ship():
    """
    Finds a set of coordinates and calls check_location() to see if its a valid spot.
    If the location is valid place it, otherwise find a new set of coordinates.  
    """
    global DEBUG
    for ship in gamemode:
        
        if R.randint(0,1) == 1: # verticle
            while True:        
                if ship == TINY_SHIP:
                    first_location = R.randint(0,89)
                    location = (first_location, first_location + 10)
                elif ship == SMALL_SHIP:
                    first_location = R.randint(0,79)
                    location = (first_location, first_location + 10, first_location + 20)
                elif ship == MEDIUM_SHIP:
                    first_location = R.randint(0,69)
                    location = (first_location, first_location + 10, first_location + 20, first_location + 30)
                elif ship == LARGE_SHIP:
                    first_location = R.randint(0,59)
                    location = (first_location, first_location + 10, first_location + 20, first_location + 30, first_location + 40)

                if DEBUG is True:
                    print("=======================")
                    print("Ship possible location" +  str(location))
                    print("=======================")

                results = check_location(ship, location)

                if DEBUG is True:
                    if results is True:
                        print("No Unsafe Spots Found!")
                        for safe_spot in location:
                            BOARD[safe_spot] = ship[-1]
                        break
                    else:
                        print("Unsafe Spots Found!")
                else:
                    if results is True:
                        for safe_spot in location:
                            BOARD[safe_spot] = ship[-1]
                        break
        else: #horrizontal 
            while True:
                if ship == TINY_SHIP:
                    while True:
                        first_location = R.randint(0,97)
                        if (first_location + 1) % 10 != 0:
                            break
                    location = (first_location, first_location + 1)
                elif ship == SMALL_SHIP:
                    while True:
                        first_location = R.randint(0,96)
                        if (first_location + 2) % 10 != 0 and (first_location + 1) % 10 != 0:
                            break
                    location = (first_location, first_location + 1, first_location + 2)
                elif ship == MEDIUM_SHIP:
                    while True:
                        first_location = R.randint(0,95)
                        if (first_location + 3) % 10 != 0 and (first_location + 2) % 10 != 0 and (first_location + 1) % 10 != 0:
                            break
                    location = (first_location, first_location + 1, first_location + 2, first_location + 3)
                elif ship == LARGE_SHIP:
                    while True:
                        first_location = R.randint(0,94)
                        if (first_location + 4) % 10 != 0 and (first_location + 3) % 10 != 0 and (first_location + 2) % 10 != 0 and (first_location + 1) % 10 != 0:
                            break
                    location = (first_location, first_location + 1, first_location + 2, first_location + 3, first_location + 4)
            
                results = check_location(ship, location)

                if DEBUG is True:
                    if results is True:
                        print("No Unsafe Spots Found!")
                        for safe_spot in location:
                            BOARD[safe_spot] = ship[-1]
                        break
                    else:
                        print("Unsafe Spots Found!")
                else:
                    if results is True:
                        for safe_spot in location:
                            BOARD[safe_spot] = ship[-1]
                        break


def check_location(type,location): 
    """
    type =  TINY_SHIP, SMALL_SHIP, MEDIUM_SHIP, LARGE_SHIP
    location = list

    Returns True if it find a suitible place for a ship and False if a ship piece is in the way.
    """
    if type == TINY_SHIP:
        loc1,loc2 = location
        loc3 = loc4 = loc5 = "empty"
    elif type == SMALL_SHIP:
        loc1, loc2, loc3 = location
        loc4 = loc5 = "empty"
    elif type == MEDIUM_SHIP:
        loc1, loc2, loc3, loc4 = location
        loc5 = "empty"
    elif type == LARGE_SHIP:
        loc1, loc2, loc3, loc4, loc5 = location

    counter = 0
    # each location is checked and will return FALSE if spot is occupied
    # If no collisions occured it will return True
    for loc in BOARD:
        if counter == loc1:
            if loc != "-":
                # print(loc)
                return False
        if counter == loc2:
            if loc != "-":
                # print(loc)
                return False
        if counter == loc3:
            if loc != "-":
                # print(loc)
                return False
        if counter == loc4:
            if loc != "-":
                # print(loc)
                return False
        if counter == loc5:
            if loc != "-":
                # print(loc)
                return False
        
        if counter  == 99:
            return True
        
        counter+= 1

def print_board():
    """
    Prints the board in a 10 by 10
    """
    for i, elem in enumerate(OBSCURD_BOARD):
        if i % 10 == 0 and i !=0:
            print(" " + str(i-10) + " - " + str(i - 1), end='') # no end of line character
            print()
        print(str(elem).ljust(3), end='') # no end of line character
    print(" " + str(i-10) + " - " + str(i), end='') # no end of line character
    print()
    if DEBUG is True:
        for i, elem in enumerate(BOARD):
            if i % 10 == 0:
                print(" " + str(i-10) + " - " + str(i - 1), end='') # no end of line character
                print()
            print(str(elem).ljust(3), end='') # no end of line character
        print(" " + str(i-10) + " - " + str(i), end='') # no end of line character
        print()

total_parts_destoryed = 0 # end game at 20

def make_choice(selector):
    """
    Return True if all parts destroyed, otherwise check for hit or miss.
    """
    global total_parts_destoryed
    global DEBUG

    if BOARD[int(selector)] != '-':
        if OBSCURD_BOARD[int(selector)] != BOARD[int(selector)]:
            total_parts_destoryed += 1
            print("-| hit! |-")
            OBSCURD_BOARD[int(selector)] = BOARD[int(selector)]
        else:
            print("You hit this already")
    else:
        print("-| Miss! |-")
    
    if total_parts_destoryed == 20:
        return True
    
def clear(): 
    """
    clears the screen
    """
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# test_location = 44,45

    
# print(results)
place_ship()
# print_board()

while True:
    print_board()
    response = input("Please enter the location to fire your missle: ") 
    clear()
    if make_choice(response)  is True:
        print("We have a Winner!")
        print_board()
        break
    