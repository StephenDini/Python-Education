# Simple pre-setup parsing to normalize the file name.


import re


def stripSpecial(TEXT):
    return re.split(r'(\[.*?\]) | (\(.*?\))', TEXT)


def stripEpisode(TEXT):
    match = re.split(r'(ep\d\d|Ep\d\d|EP\d\d|E\d\d|e\d\d)', TEXT)
    if(len(match) > 1):
        matchSpec = re.split(r'(\[\')', match[0])
        return str(matchSpec[2]).strip()


def findShowTitle(TEXT):
    match = re.compile(r'(?<=\w\\).*?(?= -|-)')
    return match.findall(TEXT)


def normalizeSpaces(TEXT):
    return TEXT.replace('_', ' ')


def findEpisode(TEXT):
    match = re.compile('(ep\d\d|Ep\d\d|EP\d\d|E\d\d|e\d\d)')
    return match.findall(TEXT)
