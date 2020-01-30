# Check if no remainder
def modCheck(x):
    if(x % 19):
        return False
    if(x % 18):
        return False
    if(x % 17):
        return False
    if(x % 16):
        return False
    if(x % 15):
        return False
    if(x % 14):
        return False
    if(x % 13):
        return False
    if(x % 12):
        return False
    if(x % 11):
        return False
    return True


# Since 20 can only be divisible by 10, we only need to increment by 20
def count():
    clicker = 20

    while(True):
        if(modCheck(clicker)):
            return clicker
        clicker = clicker + 20


print("Testing Start")
print(count())
print("Testing Finish")
