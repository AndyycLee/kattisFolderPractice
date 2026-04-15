import collections, heapq
rows, cols = map(int, input().split())

dirns = [ (1,0), (0, 1), (-1, 0), (0, -1) ]
grid = []

minMapping = [ [float("inf") for _ in range(cols)] for _ in range(rows)]
minMapping[0][0] = 0

for _ in range(rows):
    grid.append( list(map(int, input().split())  ))


heap = []
heapq.heappush(heap, (0, grid[0][0], 0, 0) ) # ladderHeight, currentHieght, posX, posY

while heap:
    ladderHeight, currentHeight, posX, posY = heapq.heappop(heap)


    if ladderHeight > minMapping[posX][posY]: continue
    if (posX, posY) == (rows - 1, cols - 1): print(ladderHeight); break

    for dr, dc in dirns:

        nr, nc = dr + posX, dc + posY
        if (0 <= nr < rows) and (0 <= nc < cols):
            
            if minMapping[nr][nc] <= ladderHeight: continue
            
            
            # now look at neighbours
            if currentHeight + ladderHeight >= grid[nr][nc]:
                heapq.heappush(heap, (ladderHeight, grid[nr][nc], nr, nc))
                minMapping[nr][nc] = ladderHeight
            else:
                higherLadder = (grid[nr][nc] - ( currentHeight + ladderHeight ))
                heapq.heappush(heap, (higherLadder + ladderHeight, grid[nr][nc], nr, nc) )
                minMapping[nr][nc] = higherLadder + ladderHeight

"""

BUGS:

TRUST UR INTUITION:
 YOU KNOW DIJKSTRAS DOESNT NEED A VSITED SET USUALLY

 YOU KNOW DIJKSTRAS WIL ALWAYS HAVE THE MINIMUM CLOSEST NODE BEING PROCESSED, MEANING
             if minMapping[nr][nc] <= ladderHeight: continue
should be <=, not <
because that means we've reached this node, with a shorter ladderHNeight before


YOU ALSO SHOULD BE MORE ASSERTIVE

LET YOURSELF TAKE MORE TIME TO DEBUG:

VERY SIMPLE ISSUE:
(grid[nr][nc] - ( currentHeight + ladderHeight ))

SUBTRACTING BRACKETS!!!!

AND INITAILIZING, MINMAPPING DICTIONARY FOR STARTINTG NODE
minMapping[0][0] = 0



"""
