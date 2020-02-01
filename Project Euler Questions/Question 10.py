# This question will provide the answer to Question 10


def isPrime(value):
    if (value < 2):
        return False
    if (value % 2 == 0):
        return value == 2
    if (value % 3 == 0):
        return value == 3
    if (value % 5 == 0):
        return value == 5
    if (value == 7):
        return True

    divisor = 7

    while(divisor * divisor <= value):
        if (value % divisor == 0):
            return False
        if (value % (divisor + 4) == 0):
            return False
        if (value % (divisor + 6) == 0):
            return False
        if (value % (divisor + 10) == 0):
            return False
        if (value % (divisor + 12) == 0):
            return False
        if (value % (divisor + 16) == 0):
            return False
        if (value % (divisor + 22) == 0):
            return False
        if (value % (divisor + 24) == 0):
            return False
        divisor += 30

    return True


# Modifying the prime finder from question 7
# will now return a string of all the numbers wanted to add
def findPrime(number):
    i = 2
    c = 1
    primeList = []
    while(c <= number):
        if(number == 2):
            primeList.append(2)  # Kind of a given
        if(isPrime(i)):
            if(i < 2_000_000):
                primeList.append(i)
            else:
                return primeList
            c = c + 1
        if(i == 2):
            i = i + 1
        else:
            i = i + 2


def listAddition(value):
    x = 0
    for i in value:
        x += i
    return x


listOfPrimes = findPrime(2_000_000)
print(listAddition(listOfPrimes))
