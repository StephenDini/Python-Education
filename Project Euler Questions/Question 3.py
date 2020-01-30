# This will provide the answer to question 3


# This will check if the number is prime
# Improved upon in question 7
def isPrime(number):
    i = 2
    while(i < number):
        if (number % i == 0 and i != number):
            # print(number)
            # print(number % 2)
            # print(i)
            return False
        elif (i == (number - 1)):
            return True
        i = i + 1

# terribly inefficiant and possibly incorrect.
# Not worth even letting it finish to test it.
# def largestFactor(number):
#     i = 2
#     held = 0
#     while(i < number):
#         if(number % i == 0):
#             if(isPrime(i)):
#                 print(i)
#                 held = i
#         i = i + 1
#     print(held)
#     return held


# Much better, instead of checking each number against 2-Number
# We find the largest Prime by finding the first
# prime that divides into the number
# Save the answer, reset to 2 and check it against the
# next prime. Repeat until x = 1.


def largestPrimeFactor(number):
    i = 2
    held = 0
    x = 0
    while (x != 1):
        if(isPrime(i)):
            if(x == 0):
                if(number % i == 0):
                    x = number / i
                    held = i
            else:
                if(x % i == 0):
                    x = x / i
                    held = i
        # print("The current value of X is: " + str(x))
        # print("Holding the highest Prime Factor Found: " + str(held))
        if(i == 2):
            i = i + 1
        else:
            i = i + 2
        if(held == i):
            i = 2
    return held


print(largestPrimeFactor(600_851_475_143))  # 600_851_475_143
