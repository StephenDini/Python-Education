# This will provide the answer to question 12
import math


def triangleNumber(value):
    return (value * (value + 1)) / 2


def FindDiv(overDiv):
    divisors = 0
    inc = 0
    new = triangleNumber(overDiv)

    while(True):
        divisors = 0
        sqrt = int(math.sqrt(new))

        for x in range(1, int(math.sqrt(new))):
            if((new % x) == 0):
                divisors += 2
        if(sqrt * sqrt == new):
            divisors -= 1

        if(divisors > overDiv):
            return new
        else:
            inc += 1
            new = int(triangleNumber(overDiv + inc))


answerNew = FindDiv(500)

print(answerNew, " is the answer")
