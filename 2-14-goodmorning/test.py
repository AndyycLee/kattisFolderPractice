# Generate all valid "typeable" numbers (right/down movement only on keypad)

choices = {1:[1,2,4], 2:[2,3,5], 3:[3,6], 4:[4,5,7], 5:[5,6,8], 6:[6,9], 7:[7,8], 8:[8,0,9], 9:[9], 0:[0]}

res = set()

def helper(curNumber):
    res.add(curNumber)
    
    lastDigit = curNumber % 10
    for choice in choices[lastDigit]:  # Only valid next digits from last digit
        potentialCurNumber = (curNumber * 10) + choice
        
        if potentialCurNumber > 10000: continue  # Need numbers beyond target to find closest
        
        helper(potentialCurNumber)

# Start from all possible first digits
for start in range(10):
    helper(start)

# Now find closest typeable number for each query
test_cases = int(input())
for _ in range(test_cases):
    target = int(input())
    # Find closest number in res to target
    closest = min(res, key=lambda x: (abs(x - target), x))
    print(closest)

