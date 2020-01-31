# This will provide the answer to Question 9
import numpy as np


# Finds a value to satify a + b + c = 100 where,
# a > b > c AND a^2 + b^2 = c^2
def findTriplet():
    for b in range(500, 0, -1):
        for a in range(500, 0, -1):
            if(a > b):
                a = b - 1
            c2 = (a * a) + (b * b)
            if((a + b + np.sqrt(c2)) == 1000):
                return (a, b, c2, a * b * int(np.sqrt(c2)))


print(findTriplet())
