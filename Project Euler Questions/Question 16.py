# This will solve Question 16
import math


container = 2**1_000

# This will add each digit that makes up the container.
def addNumbers(number):
    container = 0
    for i in str(number):
        container += int(i)

    return container

print(addNumbers(container))
