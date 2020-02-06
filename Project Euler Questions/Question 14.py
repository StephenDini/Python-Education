# This will provide the answer to question 14
def evenFunc(evenValue):
    return evenValue / 2


def oddFunc(oddValue):
    return (3 * oddValue) + 1


def findXTerm(value):
    termCounter = 0
    heldTerm = 0
    heldCounter = 0
    largerTerm = 0
    largerCounter = 0

    for i in range(2, value):
        termCounter = 0
        savedValue = i

        while(savedValue >= 1):
            if(savedValue == 1):
                heldTerm = i
                heldCounter = termCounter
                # print(heldCounter, heldTerm)
                break
            elif(savedValue % 2 == 0):
                # print(termCounter)
                savedValue = evenFunc(savedValue)
                termCounter += 1
            else:
                savedValue = oddFunc(savedValue)
                termCounter += 1

        if(heldCounter > largerCounter):
            print(heldCounter, " and ", heldTerm, " vs ", largerCounter, " and ", largerTerm)
            largerCounter = heldCounter
            largerTerm = heldTerm

    foundIt = (largerCounter, largerTerm)
    return foundIt


print(findXTerm(1_000_000))
