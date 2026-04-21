"""

do dijkstra's initialize the heap with all values of the starting row

if you reach the end, row, you finished dijkstras

we pop based on curSUm of the path

we laso a minCurrSumMap of how to reach cell

we also have a map, pointing to either None, or the node's previous cell (aka: how I reached this cell)
and that's how we're gonna do path reconstruction, to print the output fault line

"""

import heapq, sys

def solve():
    heap = []

    rows, cols = map(int, input().split() )
    if (0, 0) == (rows, cols): sys.exit()


    minCurrSumMap = [[float("inf") for _ in range(cols)] for _ in range(rows) ]

    shortestSumNodeToItsNeighbour = [[0 for _ in range(cols)] for _ in range(rows) ]
    grid = []
    for _ in range(rows):
        l = list( map(int, input()   ) )
        grid.append( l )


    for i in range(cols):
        heapq.heappush(heap, ( grid[0][i], 0, i )  ) # the actual curSum (initialized to the block's value), row, col, position
        minCurrSumMap[0][i] =  grid[0][i]
    # i'm proerply handling the edge case for if we have row length 1

    """    
    def pathReconstruct(fractureEndingRow, fractureEndingCol):

        what this does is, we've now popped the node at the last row, meaning we've found the fracture line

        look at the shortestSumNodeToItsNeighbour

        while that row isn't 0, we follow the node

        res = []
        currentRow, currentCol = fractureEndingRow, fractureEndingCol
        prevRow = 999 # dummy variable

        while currentRow != 0:
            res.append( grid[currentRow][0:currentCol] + [" "] + grid[currentRow][currentCol + 1::] )

            prevRow, prevCol = shortestSumNodeToItsNeighbour[currentRow][currentCol]
            currentRow, currentCol = prevRow, prevCol

        # im missing the starting res
        res.append(  grid[currentRow][0:currentCol] + [" "] + grid[currentRow][currentCol + 1::] )
        for frac in (reversed(res)):
            stringMaped = map(str, frac)
            print("".join(stringMaped)) # need to "".join(frac), not print(frac)

        
        while True:
            fracture_coords.add((curr_r, curr_c))
            if curr_r == 0: # Reached the top
                break
            curr_r, curr_c = shortestSumNodeToItsNeighbour[curr_r][curr_c] # we set the new coordinates, to point to the previous coords values

this three line appraoch ^^ is also way cleaner

because in: is it okay to do a while currentRow != 0 approach? or is a while True the cleanest way to handle?
Its valid Yes. , but the catch is You must add the row 0 square after the loop.
        """
    #AI says i might be missing the case where I'm supposed to go through lines multiple times?
    def pathReconstruct(fractureEndingRow, fractureEndingCol):
    # 1. Collect all coordinates belonging to the fracture line
        fracture_coords = set()
        curr_r, curr_c = fractureEndingRow, fractureEndingCol
        
        # alternatives like while if curr_r != (0, 0): would work if thats how I initialized hte parent grid, but I need to be careful for the fact that a node in row (1,1) might actually point to position (0,0), so like while curr_r != (None, None) is best
        while True:
            fracture_coords.add((curr_r, curr_c))
            if curr_r == 0: # Reached the top
                break
            curr_r, curr_c = shortestSumNodeToItsNeighbour[curr_r][curr_c] # we set the new coordinates, to point to the previous coords values

        # 2. Print the block row by row
        for r in range(rows):
            output_row = []
            for c in range(cols):
                if (r, c) in fracture_coords:
                    output_row.append(" ")
                else:
                    output_row.append(str(grid[r][c]))
            print("".join(output_row))
        print() # Blank line after each block

    
    dirns = [ (1,0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1) ]
    while heap:
        curMinSum, r, c = heapq.heappop(heap)

        if r == ( rows - 1 ): # we've reached the end, because the way dijkstras works is poppign the node means it was the "vistied" shortest way to reach it
            # now we need to do path reconstruction
            pathReconstruct(r, c)
            break

        if minCurrSumMap[r][c] < curMinSum: continue

        for dr, dc in dirns:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows) and (0 <= nc < cols) and minCurrSumMap[nr][nc] > curMinSum + grid[nr][nc]:

                # this mean's we can relax this edge, it's the shortest way we've found to reach it so far (but not guaranteed to be the shortest path ever to reach this node ever?
                # i think even in this modified dijkstras the shortest way to ever reach it, even though the cell's themslves have the weight, instead of the path itself)
                newSum = curMinSum  + grid[nr][nc]

                heapq.heappush(heap, (newSum, nr, nc))
                # relax the edge, and mark the neighbour node, wiht the prev index
                minCurrSumMap[nr][nc] = newSum
                shortestSumNodeToItsNeighbour[nr][nc] = (r, c)

                """
                WHAT WAS THE ISSUE WITH?
                curMinSum  = curMinSum  + grid[nr][nc]
                
                but using:
                newSum = curMinSum  + grid[nr][nc]
                fixes it

                and that's because, in the old version, we are overwriting curMinSum, therby resulting in when the for loop cheeck's other directions, it uses the previous for loop thingy and accidentally keeps adding curMinSum
                """
    

# test = [0,1,2,3,4,5,6,7,8]
# print(test[0:4] + [" "] + test[5:])
while True:
    solve()

    """
    Unfortuante I couldn't get that one due to path reconstruction

    Your code assumed a 1:1 relationship between a step in your backtrack and a row in the output
    In your mind, the path was likely a straight-ish line from top to bottom. But because the fracture can move in 8 directions (including sideways and back up), that assumption broke.


1. The "One Step = One Row" Fallacy
In your while loop, every time you moved to a prevRow, you appended a line to res.

Your Logic: "I found a piece of the fracture, so I'll create a row for it."

The Problem: If a fracture line visits three different squares in Row 5, your loop runs three times for Row 5. You end up with three separate versions of Row 5 in your res list. When you print it, your block looks "stretched" or duplicated.

Since the path can move diagonally up or sideways, the "fracture line" is a sequence of coordinates, not a sequence of rows.If the path looks like this: $(0,1) \rightarrow (1,1) \rightarrow (1,2) \rightarrow (2,2)$, Row 1 is visited twice.Your approach would print: Row 0, then Row 1, then Row 1 again, then Row 2.The correct approach must print: Row 0, then Row 1 (with two spaces), then Row 2.

Your code can't handle a row having two or more holes in it.


which makes sense, because my bugs were the fact I append each row's path state

rather than a singular row with all hte holes


    """