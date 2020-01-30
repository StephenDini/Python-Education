# This will provide the answer to question 2


i = 1
old = 1
total = 0
held = 0


while(i < 4000000):
    # held = i
    # i = i + old
    # old = held

    # this works as such i will be equal to the value of i + old and
    # old will equal the value of i before the addition.
    # much shorter to write than the above.
    (i, old) = (i + old, i)

    # print("I: " + str(i) + "\nOld: " + str(old))

    if(i % 2 == 0):
        total = i + total

print(total)
