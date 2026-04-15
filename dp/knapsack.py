import sys
from functools import cache

amount, numOfTestCases = int(input().split())


@cache
def helper(amountLeft, i):

    if amountLeft <0:
        return float('inf')
    if i == numOfTestCases:
        return 0
    
    # choose stone
    choose = helper(amountLeft - arr[i][1], i + 1) + arr[i][0]

    #skip stone
    skip = helper(amountLeft, i + 1)

    if choose > skip:
        decisions[ (   amountLeft , i     )  ] = "take"
        return choose
    else:
        decisions[  ( amountLeft , i    )  ] = "skip"
        return skip

while True:
    arr = []

    decisions = {}

    for _ in range(numOfTestCases):
        value, weight = map(int, input().split())
        arr.append( (value, weight) )
    helper(amount, 0)

    helper.cache_clear()  # clear between test cases!

        