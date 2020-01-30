# This will provide the answer to question 6


# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
def sumOfSquares(x):
    held = 0
    for i in range(1, x + 1):
        held = (i * i) + held

    return held


# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
def squareOfSum(x):
    held = 0
    for i in range(1, x + 1):
        held = i + held
    return held * held


# squareOfSum() - sumOfSquares(x)
def ssDif(x):
    return squareOfSum(x) - sumOfSquares(x)


input = 100
print(f'{sumOfSquares(input):,}')
print(f'{squareOfSum(input):,}')
print(f'{ssDif(input):,}')
