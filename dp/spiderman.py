"""

SOME REFLECTIONS:

I previously observed after reflecting its resemblence to COIN CHANGE 1, but we return choices, rather than in coin change returning the minNumberOFCoins we can use

I already spent alot of tiem prior ideating (roughly 1 or 2 days after passively reading the problem)

I want to test my coding speed, it's 11PM rn

SOME OBSERVATION I DID WHILE THINKING OF THIS PROBLEM OVERNIGHT AND OVERDAY AFTER READING IT PRIOR:


20 20 20 20

is split string conveted into -> array input

at each step, you can choose
go UP
or go DOWN

and mark this choice you make as:
"U" or "D"

if runningSum is <0, return float(inf)


return the valid string, if we reach end of array ( i == n = len(arr))


BECAUSE i need to return the outcome of both choices we make
and the currentTotal since we want to minimize the height

our return value is two things
(currentHeight, choicesTaken)
"""
from functools import cache

numOfTestCases = int(input())


for _ in range(numOfTestCases):
    n = int(input())

    spiderManJumpArr = list(map(int, input().split()) )

    @cache
    def helper(i, curSum):
        # base cases
        if curSum < 0: return (float("inf"), "IMPOSSIBLE" )

        if i == n and curSum == 0: return (0, "")

        if i == n: return (float("inf"), "IMPOSSIBLE")

        # my choices of either going up, or down

        chooseUp = helper(i + 1, curSum + spiderManJumpArr[i])

        chooseUpCurrTotal, chooseUpChoices = chooseUp

        chooseDown = helper(i + 1, curSum - spiderManJumpArr[i])

        chooseDownCurrTotal, chooseDownChoices = chooseDown

        # return the min of these choices

        if chooseUpCurrTotal > chooseDownCurrTotal:
            return (chooseUpCurrTotal - spiderManJumpArr[i], chooseDownChoices + "D")

        else:
            return (chooseDownCurrTotal + spiderManJumpArr[i], chooseUpChoices + "U")

    currentHeight, choices = helper(0, 0)

    if currentHeight != float("inf"):
        print(choices)
    else:
        print("IMPOSSIBLE")


