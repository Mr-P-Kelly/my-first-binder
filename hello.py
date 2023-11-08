import math

def prime( num ):
    if num < 2:
        return False
    for ii in range(2,math.floor(math.sqrt(num)+1 )):
        if num % ii == 0:
            return False
    return True

for jj in range(145):
    if prime(jj):
        print(jj, " is Prime")
