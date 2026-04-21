"""

because this is union find,

I'm mapping each cell in the grid, to it's POND

what this means is for connected cells, they are part of hte same pond

I was thinking, I could do this either with a grid

where parent[i][j] = parent of that cell

and rankGrid, where the i,j of that cell is the rank of that cell's parent

and while that's technically faster

the dictionary version feels more intutive

where I map acell to it's parent

(i, j) : parentCell (i, j)

and rank is set by a rankMap
where (i, j): thisCell'sParent's ranking

"""
import sys

# You MUST have this for the recursive find to work on large grids

rows, cols = map(int, input().split())


parent = []
parentRank = []

grid = []
for r in range(rows):
    line = list(map(int, list(input())))
    grid.append(line)
    
    # Initialize the rows for parent and parentRank as we read the grid
    parent.append([(r, c) for c in range(cols)])
    parentRank.append([0] * cols)

def find(r, c):
    # Base case: if the cell is its own parent
    if parent[r][c] == (r, c):
        return (r, c)

    # Path compression: update parent[r][c] to the ultimate root
    root_r, root_c = parent[r][c]
    parent[r][c] = find(root_r, root_c)
    return parent[r][c]

def union(rA, cA, rB, cB):
    rootA = find(rA, cA)
    rootB = find(rB, cB)

    if rootA == rootB: return

    rA_p, cA_p = rootA
    rB_p, cB_p = rootB

    if parentRank[rA_p][cA_p] > parentRank[rB_p][cB_p]:
        parent[rB_p][cB_p] = rootA
    elif parentRank[rB_p][cB_p] > parentRank[rA_p][cA_p]:
        parent[rA_p][cA_p] = rootB
    else:
        parent[rB_p][cB_p] = rootA
        parentRank[rA_p][cA_p] += 1


dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(rows):
    for j in range(cols):
        cellType = grid[i][j]
        for dr, dc in dirns:
            nr, nc = dr + i, dc + j
            if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == cellType:
                union(i, j, nr, nc)

numOfQueries = int(input())

for _ in range(numOfQueries):
    r1, c1, r2, c2 = map(int, input().split())

    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    # FIXED: Check grid[r1][c1] instead of the diagonal grid[r1][c2]
    if grid[r1][c1] != grid[r2][c2]: 
        print("neither")
    else:
        cell1Parent = find(r1, c1)
        cell2Parent = find(r2, c2)

        if cell1Parent != cell2Parent:
            print("neither")
        else:
            if grid[r1][c1] == 0:
                print("binary")
            else:
                print("decimal")




"""
unfortunately, this gets TLE still

the one other optimziation I think of is using the grid as a dict mapping, rather than thedictionary 

im too tired to code this up, so i used AI to translate to my version

below was mine:


parent = {}
parentRank = {}

def find(cell):
    if cell not in parent:
        parent[cell] = cell
        parentRank[cell] = 0

    if parent[cell] == cell: return cell

    parent[cell] = find( parent[cell] )

    return parent[cell]

def union(cellA, cellB):
    cellAParent, cellBParent = find(cellA), find(cellB)

    if cellAParent == cellBParent: return

    if parentRank[cellAParent] > parentRank[cellBParent]:
        # union B's parent to A's
        parent[cellBParent] = cellAParent
    elif parentRank[cellBParent] > parentRank[cellAParent]:
        parent[cellAParent] = cellBParent
    
    else:
        parent[cellBParent] = cellAParent
        parentRank[cellAParent] += 1

grid = []

rows, cols = map(int, input().split())

for _ in range(rows):
    l = list( map(int, list(input()) )  )

    grid.append(l)

dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(rows):
    for j in range(cols):

        cellType = grid[i][j]

        # now look at neighbours for each cell
        for dr, dc in dirns:
            nr, nc = dr + i, dc + j

            if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == cellType:
                union( (nr, nc), (i, j) )


numOfQueries = int(input())

for _ in range(numOfQueries):
    r1, c1, r2, c2 = map(int, input().split() )

    r1, c1, r2, c2 = r1 -1, c1 -1, r2 -1, c2 -1

    if grid[r1][c1] != grid[r2][c2]: print("neither")
    else:
        cell1Parent, cell2Parent = find( (r1, c1) ), find( (r2, c2) )

        cellsType = grid[r1][c1] # stupid bud, it was set to grid[r1][c2]

        if cell1Parent != cell2Parent:
            print("neither")
        
        else:
            if cellsType == 0:
                print("binary")
            else:
                print("decimal")
"""