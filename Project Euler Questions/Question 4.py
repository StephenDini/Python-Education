# This will provide the answer to question 6


# Legibility function only
# it could always be used the normal way but now why it is used
# is easily gathered.
def palindrome(x):
    return str(x) == str(x)[::-1]


# Largest palindrome product
# Checks if i * x will solve into a palindrome.
# from highest to smallest, it will check each i for all of x
# within the digit limit.
def lPP(size):
    z = 0
    c = 1
    container = [(0, 0, 0)]
    while(z < size):
        c = str(c) + str(0)
        print(c)
        z = z + 1

    for i in reversed(range(int(c))):
        if(i > (int(c) / 10)):
            for x in reversed(range(int(c))):
                if(x > (int(c) / 10)):
                    if(palindrome(i * x)):
                        container.append([i, x, (i * x)])
    container.sort(key=lambda x: x[2])
    return container.pop()


(value1, value2, value3) = lPP(3)

print(str(value1) + ' * ' + str(value2) + ' = ' + str(value3))
