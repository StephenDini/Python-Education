# This will provide the answer to question 15
import pprint


mazeSmall = [[0] * 3 for i in range(0, 3)]
pprint.pprint(mazeSmall)
mazeLarge = [[0] * 21 for i in range(0, 21)]

# if(str(input("Would you like to enter a custom square?")).lower == "y"):
#     customValue = input("Please enter a whole number.")
# mazeCustom = [[0] * (customValue + 1) for i in range(0, customValue + 1)]


# only allowed to move down and right
def findAllPaths(maze):
    size = len(maze) - 1
    path = []
    allPaths = []
    print(len(path), "asdasd")
    # while(true):


    # return size

print(mazeLarge[20][20])
pprint.pprint(findAllPaths(mazeLarge))
