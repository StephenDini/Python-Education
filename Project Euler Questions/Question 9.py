import numpy as np

def findTriplet():
    #for c in range(500, 0, -1):
    for b in range(500, 0, -1):
        for a in range(500, 0, -1):
            # (a, b, c) =  (i - 2, i-1, i)
            # if(b > c):
            #     b = c - 1
            if(a > b):
                a = b - 1
            c2 = (a*a)+(b*b)
            if((a + b + np.sqrt(c2)) == 1000):
                print("location Found")
                print(a,b,c2)
                print("a^2 + b^2 : ",(a*a)+(b*b), "c^2 : ", (c2))
                print("Moving on")
            else:
                print(np.sqrt(c2)," + ", b," + ", a, "not found")

print(findTriplet())
