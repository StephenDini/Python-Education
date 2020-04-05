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
# Will sort multiple paths INPROG
sortPaths = ['E:\Anime']

# List of paths that will be iterated through.
sortablePaths = []

# List containing the Files, Folders, and Dirs
allFolders = []
allDirs = []
allFiles = []

# List of Directories that are a possible match to the File
matchedDirs = []

# Find the paths for each folder inside the directories.
# MULTIPLE DIRECTORS NOT IMPLEMENTED
for currPaths in sortPaths:
    sortablePaths = Path(currPaths)
    testDir = list(sortablePaths.glob('*.*'))

# Walk the Directories
for dir, subDir, files in os.walk('E:\Anime'):
    for dirName in dir:
        allDirs.append(dirName)
    for folderName in subDir:
        allFolders.append(folderName)
    for fileName in files:
        allFiles.append(fileName)

# Set regex to search for only certain files
regex = re.compile(r'(.db|.avi|.mp4|.mkv)')
# regexFileExtensions = re.compile(r'(.avi|.mp4|.mkv)')

# print(testDir)

# Searches through the directories for the matching file extensions.
for x in testDir:
    tester = regex.findall(str(x))
    # print(tester)

    # Catch the invisible thumbnail files and do nothing
    if(tester == ['.db']):
        print('---------------------------------------------------')
        print()
        print('---------------------------------------------------')
        print('Found a Thumbnail, disregarding')

    # Catch the correct file path and sort it
    elif(tester == ['.mkv'] or ['.avi'] or ['.mp4']):

        # Before split
        print("Before Split: " + str(x))

        # split once
        firstSplit = nf.findShowTitle(str(x))
        print("After First Split: " + str(firstSplit))

        # Last Split to extract just the title.
        title = nf.stripEpisode(str(firstSplit))
        print("After Last Split: " + str(title))

        if title:
            print('---------------------------------------------------')
            print()
            print('---------------------------------------------------')
            print('Found a Video')
            print('File Path: ' + str(x))

            # print(firstSplit)
            print('Title Only: ' + str(title))

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