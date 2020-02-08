import math


container = 2**1_000

print(container)
def addNumbers(number):
    container = 0
    for i in str(number):
        container += int(i)

    return container

print(addNumbers(container))
