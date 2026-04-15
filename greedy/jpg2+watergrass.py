class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

# THESE ARE THE PATTERNS FOR GREEDY EXPANSION

import sys
import math

for line in sys.stdin:
    if not line.strip():
        continue

    n, l, w = map(int, line.split())
    intervals = []

    for _ in range(n):
        x, r = map(int, sys.stdin.readline().split())

        # If radius too small, it cannot cover full width
        if r <= w / 2:
            continue

        dx = math.sqrt(r*r - (w/2)*(w/2))
        left = x - dx
        right = x + dx
        intervals.append((left, right))

    # Sort by left endpoint
    intervals.sort()

    current_end = 0
    count = 0
    i = 0
    m = len(intervals)

    while current_end < l:
        farthest = current_end

        while i < m and intervals[i][0] <= current_end:
            farthest = max(farthest, intervals[i][1])
            i += 1

        if farthest == current_end:
            print(-1)
            break

        current_end = farthest
        count += 1

    else:
        print(count)

# import math
# while True:
#     n, length, w = map(int, input().split())
#     curLength, count = 0, 0
    
#     grassSprinkleList
#     for _ in range(n):
#         # now at each step, we need to make the choice from 0, seeing if we can reach the length
#         # and we try to pick the overlapping radius which is largest
#         # we can find the horizontal length by doing
        
#         position, radius = map(int, input().split())
        
#         horizontalLength = math.sqrt( (radius**2) - ((w/2)**2 ))
        
    
#     if curLength < length: print(-1)
#     else: print(count)


"""
something worth noting in jumpgame2
if we could fail, I'd need a check like:
if farthest == currentEnd:
    return -1

or if farthest == r:

because in jumpgame2, our check is: farthest = max(farthest, i + nums[i])

due to : for i in range(l, r + 1): farthest = max(farthest, i + nums[i])
so worst case scenario, our farthest jump is just i, which is just r

thats why I dont need farthest <= r, because farthest will always be at least size  r

"""