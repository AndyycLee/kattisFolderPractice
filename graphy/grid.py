"""
level-order BFS

instead of BFS that stores count, position in each state

"""
import sys, collections

rows, cols = map(int, input().split())

grid = [[0 for _ in range(cols)] for _ in range(rows)]


for r in range(rows):
    line = sys.stdin.readline().strip()
    for c, colValue in enumerate(line):
        grid[r][c] = int(colValue)


# now do a modified level-order bfs, starting with the top square, and going to the bottom

def bfs():
    visited = set( (0,0) )
    dirns = [(1,0), (0, -1), (-1, 0), (0, 1)]

    q = collections.deque([ (0,0) ])
    count = 0
    while q:
        count += 1
        for _ in range(len(q)):
            r, c = q.popleft()

            jumpMultiplier = grid[r][c]
            for dr, dc in dirns:
                nr, nc = ((dr*jumpMultiplier) + r), ((jumpMultiplier*dc) + c)

                if (0 <= nr < rows) and (0 <= nc < cols) and (nr, nc) not in visited:
                    
                    if (nr, nc) == (rows -1, cols-1): return count

                    # then we can go here so
                    visited.add( (nr, nc) )
                    q.append( (nr, nc) )
    return -1

print(bfs())


"""
bugs:

didn't parse input correctly, assumed it was space seperated like
1 1 1 1

it was: 1111


BIG BUG:
bottom-right square is at (rows - 1, cols - 1) not (rows, cols)

"""