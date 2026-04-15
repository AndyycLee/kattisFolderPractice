
choices = {
    1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    2: [2, 3, 5, 6, 8, 9, 0],
    3: [3, 6, 9],
    4: [4, 5, 6, 7, 8, 9, 0],
    5: [5, 6, 8, 9, 0],
    6: [6, 9],
    7: [7, 8, 9, 0],
    8: [8, 9, 0],
    9: [9],
    0: [0]
}
res = set()

def helper(curNumber):
    
    # if curNumber > 200:
    #     continue

    # base case, add the number to our res
    res.add(curNumber)
    
    lastDigit = curNumber % 10
    for choice in choices[lastDigit]:  # Only valid moves from last digit
        potentialCurNumber = (curNumber * 10) + choice
        
        if potentialCurNumber > 200: continue
    
    
        helper(potentialCurNumber)
        
        # skip
        # helper(curNumber)
helper(1)
helper(2)
helper(3)
helper(4)
helper(5)
helper(6)
helper(7); helper(8); helper(9)
# helper(0) - would cause a infinite recursive loop with choice of 0

sorted_list = sorted(res)

test_cases = int(input())
for _ in range(test_cases):
    
    target = int(input())

    if target in res:
        print(target)
    else:
        # run a binary search on the sorted set
        # so that i can now find the closest number
        # but its a bit of a modified binary search as we will never be able
        # to actually reach the target number, but rather just our condition is if we find both
        # positions greater and less than it, meaning the closest must be between those 2
        
        l, r = 0, len(sorted_list) -1
        
        while l <= r:
            m = (l + r) // 2
            if m == 0 or m == len(sorted_list) -1:
                print(sorted_list[m])
                break
            # and r < len(sorted_list) -1 - this is unnecessary
            if l > 0  and (target > sorted_list[m-1]) and (target < sorted_list[m]):
                if (target - sorted_list[m-1]) > (sorted_list[m] - target):
                    print(sorted_list[m])
                    break
                else:
                    print(sorted_list[m-1])
                    break
            elif target > sorted_list[m]:
                l = m + 1
            else:
                r = m -1
        
                

# def helper(curNumber, lastDigit):
#     res.add(curNumber)
    
#     for choice in choices[lastDigit]:
#         potentialCurNumber = (curNumber * 10) + choice
        
#         if potentialCurNumber > 200: continue
        
#         helper(potentialCurNumber, choice)  # choice becomes the new lastDigit

# # Then call as:
# for d in range(1, 10):
#     helper(d, d)