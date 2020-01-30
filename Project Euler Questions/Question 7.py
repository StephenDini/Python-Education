# This will provide the answer to question 7
# For this we will use the function that was
# created for question 3 but fixed the incorrect
# way I was handling it # turns out this was the slow down.


# def isPrime(number):
#     i = 2
#     while(i <= number):
#         if (number % i == 0 and i != number):
#             # print(number)
#             # print(number % 2)
#             # print(i)
#             return False
#         elif (i == (number)):
#             print(str(i) + " : " + str(i))
#             return True
#         i = i + 1

# This works far better than what I devised. (90s saved.)
# but why is this recommended at
# https://codereview.stackexchange.com/questions/124644/project-euler-7-10001st-prime
# Everything but the while loop is a given but
# why checking just that loop works to validate the prime?


def isPrime(value):
    # reason: Check for multiples of 2, 3, 5 and 7 (incrementing by 30)
    # no reason to waste time checking what is easily known.
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

    # reason: When removeing the previous (and multiples of 7(+30) thereon)
    # We can use this pattern to check against the assumed prime
    # since these are the known Prime locations
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

# So this works but it will take for ever. Could it be done faster?
# Time to finish 97.5s not bad but what if you do something outragous?
# Fixing isPrime drastically sped it up


def findPrime(number):
    i = 2
    c = 1
    while(c <= number):
        if(number == 2):
            return 2  # Kind of a given
        if(isPrime(i)):
            if(c == number):
                return i
            c = c + 1
        if(i == 2):
            i = i + 1
        else:
            i = i + 2


location = 10_001

print("The " + str(location) + " prime number is " + str(findPrime(location)))
