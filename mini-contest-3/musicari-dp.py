concertLength, numOfMusicians = map(int, input().split())
musiciansBreakTime = list( map(int, input().split()) )

pathReconstruction = {}

def helper(i, inteval1, interval2):
    if i == numOfMusicians:
        return True
    
    if interval1 > concertLength or interval2 > concertLength:
        return False

    chooseInterval1, chooseInterval2 = False, False

    chooseInterval1 = helper(i + 1, inteval1 + musiciansBreakTime[i], interval2)
    chooseInterval2 = helper(i + 1, inteval1, interval2 + musiciansBreakTime[i])

    return chooseInterval1 or chooseInterval2
# abovce is missing path reconstruction, we need to know which choice we made at each step to reconstruct the solution

"""
from functools import cache

concertLength, numOfMusicians = map(int, input().split())
musiciansBreakTime = list(map(int, input().split()))

choices = {}

@cache
def helper(i, interval1, interval2):
    # Invalid state: one interval already too long
    if interval1 > concertLength or interval2 > concertLength:
        return False

    # All musicians placed successfully
    if i == numOfMusicians:
        return True

    t = musiciansBreakTime[i]

    # Try putting musician i in interval 1
    if helper(i + 1, interval1 + t, interval2):
        choices[(i, interval1, interval2)] = 1
        return True

    # Try putting musician i in interval 2
    if helper(i + 1, interval1, interval2 + t):
        choices[(i, interval1, interval2)] = 2
        return True

    return False


possible = helper(0, 0, 0)

if not possible:
    print("impossible")
else:
    # Reconstruct one valid arrangement
    result = [0] * numOfMusicians
    interval1, interval2 = 0, 0

    for i in range(numOfMusicians):
        decision = choices[(i, interval1, interval2)]

        if decision == 1:
            result[i] = interval1
            interval1 += musiciansBreakTime[i]
        else:
            result[i] = interval2
            interval2 += musiciansBreakTime[i]

    print(" ".join(map(str, result)))
what this means is, taking 
a look at the future, and if it suceeded making the current preesent show the next choice with 
choices[(i, interval1, interval2)] = 1  # went to interval1?

"""