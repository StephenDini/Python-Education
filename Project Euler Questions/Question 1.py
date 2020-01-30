# This will provide the answer to question 1
i = 0
three = 0
five = 0
both = 0


while(i < 1000):
    if((i % 3) == 0 and (i % 5) == 0):
        both += i
    elif((i % 3) == 0):
        three += i
    elif((i % 5) == 0):
        five += i
    i = i + 1

total = five + three + both

print("The answer to problem one is " + str(total))
