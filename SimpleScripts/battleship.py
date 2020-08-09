import random as R
import pprint as pp


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

TINY_SHIP = 'TT'
SMALL_SHIP = 'SSS'
MEDIUM_SHIP = "MMMM"
LARGE_SHIP = "LLLLL"
DEBUG = True

gamemode = [TINY_SHIP, MEDIUM_SHIP, MEDIUM_SHIP, LARGE_SHIP, LARGE_SHIP]

def place_ship():
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
                        # print(first_location)
                        if (first_location + 4) % 10 != 0 and (first_location + 3) % 10 != 0 and (first_location + 2) % 10 != 0 and (first_location + 1) % 10 != 0:
                            # print("==========")
                            # print(first_location + 1)
                            # print("==========")

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


# returns True if no unsafe locations are found, False if a ship is already in the spot
def check_location(type,location): 
    
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
                print(loc)
                return False
        if counter == loc2:
            if loc != "-":
                print(loc)
                return False
        if counter == loc3:
            if loc != "-":
                print(loc)
                return False
        if counter == loc4:
            if loc != "-":
                print(loc)
                return False
        if counter == loc5:
            if loc != "-":
                print(loc)
                return False
        
        if counter  == 99:
            return True
        
        counter+= 1

# Prints the board in a 10 by 10
def print_board():
    for i, elem in enumerate(BOARD):
        if i % 10 == 0:
            print()
        print(str(elem).ljust(3), end='')
    print()

        
# test_location = 44,45

    
# print(results)
place_ship()
print_board()


