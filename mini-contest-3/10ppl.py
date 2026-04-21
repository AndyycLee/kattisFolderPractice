"""
looks like a standard BFS between those two given locations

where I try to identify if a path exists

obviously a path won't exist if the numbers have different values (0, 1)


but a path can exist with the same values at the grid

the given positions are also one indexed
"""



rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    line = map(int, list(input()))
    grid.append( list(line) )

import collections


dirns = [(1, 0), (-1, 0), (0, 1), (0, -1)]

decimalGlobalValidVisited = set()
binaryGlobalValidVisited = set()

def bfs(r, c, target):
    typeOfNum = grid[r][c]

    if typeOfNum == 0:
        globalValidVisited = binaryGlobalValidVisited

    else:
        globalValidVisited = decimalGlobalValidVisited

    if (r, c) == target:
        globalValidVisited.add(target)
        return True

    visited = set()
    visited.add( (r, c) )

    q = collections.deque()

    q.append( (r, c) )

    while q:
        row, col = q.popleft()

        for dr, dc in dirns:
            nr, nc = dr + row, dc + col

            if (0 <= nr < rows) and (0 <= nc < cols) and ((nr, nc) not in visited) and grid[nr][nc] == typeOfNum:
                
                if (nr, nc) in globalValidVisited:
                    if typeOfNum == 0:
                        binaryGlobalValidVisited.update(visited)
                    else:
                        decimalGlobalValidVisited.update(visited)
                    return True

                if (nr, nc) == target:
                    visited.add( (nr, nc) )
                    if typeOfNum == 0:
                        binaryGlobalValidVisited.update(visited)
                    else:
                        decimalGlobalValidVisited.update(visited)
                    return True

                q.append( (nr, nc ) )
                visited.add( (nr, nc) )
    return False

numOfQueries = int(input())

for _ in range(numOfQueries):
    r1, c1, r2, c2 = map(int, input().split())

    # minus one for 0 index offset
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 -1, c2 - 1

    if grid[r1][c1] != grid[r2][c2]:
        print("neither")

    else:
        if grid[r1][c1] == 1:
            if (r1, c1) in decimalGlobalValidVisited and (r2, c2) in decimalGlobalValidVisited:
                print("decimal")
            elif bfs(r1, c1, (r2, c2) ):
                print("decimal")
            
            else:
                print("neither")
        else:
            if (r1, c1) in binaryGlobalValidVisited and (r2, c2) in binaryGlobalValidVisited:
                print("binary")
            elif bfs(r1, c1, (r2, c2) ):
                print("binary")
            
            else:
                print("neither")
"""
TLE on testcase 22

potential optimziaiton I could make

using a visited dictionary map, instead of a set? but this shouldnt be a big time save

a bigger time save!:

using a type of unique global visited set, so I can check answers fast if we've explored this path before

"""