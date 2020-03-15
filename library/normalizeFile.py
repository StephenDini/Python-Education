# Simple pre-setup parsing to normalize the file name.


import re


def stripSpecial(TEXT):
    # match = re.compile(r'(\[.*?\])'))
    # return match.findall(TEXT)
    return re.split(r'(\[.*?\]) | (\(.*?\))', TEXT)


def stripEpisode(TEXT):
    match = re.split(r'(ep\d\d|Ep\d\d|EP\d\d|E\d\d|e\d\d)', TEXT)
    # holder = match.match(TEXT)
    if(len(match) > 1):
        matchSpec = re.split(r'(\[\')', match[0])
        # print(matchSpec[2])
        return matchSpec[2]


def findShowTitle(TEXT):
    match = re.compile(r'(?<=\w\\).*?(?= -|-)')
    return match.findall(TEXT)


def normalizeSpaces(TEXT):
    return TEXT.replace('_', ' ')
    # TEXT.replace('-', ' ')


def findEpisode(TEXT):
    match = re.compile('(ep\d\d|Ep\d\d|EP\d\d|E\d\d|e\d\d)')
    return match.findall(TEXT)


# test = "[this is a test] This_should_not_be_found (thest) EP01"
# test2 = stripSpecial(test)
# print(normalizeSpaces(str(test2)))
# print(findEpisode(test))
