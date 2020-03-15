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


# Directory Location(s)
sortPaths = ['E:\Anime']
sortablePaths = []

for currPaths in sortPaths:
    sortablePaths = Path(currPaths)
    testDir = list(sortablePaths.glob('*.*'))

regex = re.compile(r'(.db|.avi|.mp4|.mkv)')
# regexFileExtensions = re.compile(r'(.avi|.mp4|.mkv)')

print(testDir)

for x in testDir:
    tester = regex.findall(str(x))
    print(tester)
    if(tester == ['.db']):
        print('Found a Thumbnail')
    if(tester == ['.mkv'] or ['.avi'] or ['.mp4']):
        print('Found a Video')
        print('File Path: ' + str(x))

        firstSplit = nf.findShowTitle(str(x))
        title = nf.stripEpisode(str(firstSplit))

        # print(firstSplit)
        print('Title Only: ' + str(title))

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