# This can organize/move files.
# and in the future maintain a storage drive's structure
#
# It will organize Video files into
# Videos > Movies > Genre > SHOW NAME
# Videos > Tv Shows > Genre > SHOW NAME
# Videos > Anime > Genre > SHOW NAME
from pathlib import Path
import sys
import re
sys.path.insert(1, 'D:\Projects\Dev\Python Education\library')
import normalizeFile as nf


# Directory Location(s)
sortPaths = ['E:\Anime']
sortablePaths = []

for currPaths in sortPaths:
    sortablePaths = Path(currPaths)
    testDir = list(sortablePaths.glob('*.*'))

regex = re.compile(r'(.db)')
print(testDir)
for x in testDir:
    tester = regex.findall(str(x))
    print(tester)
    if(tester != ['.db']):
        print(True)


# Check for files in the root level of the directory
# for currPaths in sortablePaths:
#     for x in currPaths:
#         files = list(x.glob('*.*'))

# print(x)
# regex = re.compile(r'.db')
# testMatch = regex.match()