# This can organize/move files.
# and in the future maintain a storage drive's structure
#
# It will organize Video files into
# Videos > Movies > Genre > SHOW NAME
# Videos > Tv Shows > Genre > SHOW NAME
# Videos > Anime > Genre > SHOW NAME
# Files of a series need will to have its show name in its name.

from pathlib import Path
import sys
import re
import shutil
import os

sys.path.insert(1, 'C:\Dev\Python-Education\library')
import normalizeFile as nf
from fuzzywuzzy import fuzz

# Directory Location(s)
sortPaths = ['E:\Anime']
sortablePaths = []
allFolders = []
allDirs = []
allFiles = []
matchedDirs = []


for currPaths in sortPaths:
    sortablePaths = Path(currPaths)
    testDir = list(sortablePaths.glob('*.*'))

for dir, subDir, files in os.walk('E:\Anime'):
    for dirName in dir:
        allDirs.append(dirName)
    for folderName in subDir:
        allFolders.append(folderName)
    for fileName in files:
        allFiles.append(fileName)

regex = re.compile(r'(.db|.avi|.mp4|.mkv)')
# regexFileExtensions = re.compile(r'(.avi|.mp4|.mkv)')

print(testDir)

for x in testDir:
    tester = regex.findall(str(x))
    # print(tester)
    if(tester == ['.db']):
        print('---------------------------------------------------')
        print()
        print('---------------------------------------------------')
        print('Found a Thumbnail, disregarding')
    elif(tester == ['.mkv'] or ['.avi'] or ['.mp4']):
        firstSplit = nf.findShowTitle(str(x))
        title = nf.stripEpisode(str(firstSplit))
        if title:
            print('---------------------------------------------------')
            print()
            print('---------------------------------------------------')
            print('Found a Video')
            print('File Path: ' + str(x))

            # print(firstSplit)
            print('Title Only: ' + str(title))
        # if( title == "Rosario to Vampire"):
        #     print("we do not have a problem")
        # else:
        #     print("we have a problem.")

        #  Find if folder exits for found title
            for i in allFolders:
                if fuzz.ratio(i, title) >= 90:
                    print(title)
                    print("A folder already exists.")
                    print(fuzz.ratio(i, title))
                    if len(matchedDirs) > 1:
                        matchedDirs = []
                elif fuzz.partial_ratio(i,title) > 90:
                    print("Saving possible match:  " + i)
                    matchedDirs.append(i)

            if len(matchedDirs) > 1:
                choiceNumber = 1

                print('0: Create a new Folder')

                for i in matchedDirs:
                    print(str(choiceNumber) + ': ' + i)
                    choiceNumber += 1

                heldInput = -1
                while heldInput < 0 or heldInput > len(matchedDirs):
                    try:
                        heldInput = int(input('Please enter the correct folder number, use 0 if you would like to '
                                              'create a new folder.'))
                        print('Your choice was: ' + str(heldInput))
                    except ValueError:
                        print('A number between 0 and ' + str(len(matchedDirs)) + ' is required')


                matchedDirs = []


        # shutil.move()


# for dirpath, dirnames, files in os.walk('E:\Anime'):
#     if files:
#         print(dirpath, 'has files')
#     if not files:
#         print(dirpath, 'is empty')

# Check for files in the root level of the directory
# for currPaths in sortablePaths:
#     for x in currPaths:
#         files = list(x.glob('*.*'))

# print(x)
# regex = re.compile(r'.db')
# testMatch = regex.match()