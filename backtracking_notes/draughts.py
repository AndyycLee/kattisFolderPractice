import sys

numOfTestCases = int(input())

maxCount = [0]

dirns = [ (-1, -1), (-1, 1), (1, -1), (1, 1) ]

for _ in range(numOfTestCases):
    board = []
    # need to read the whiteline space
    sys.stdin.readline()

    for _ in range(10):
        board.append( list(input()) )

    def backtrack(r, c):
        maxCount[0] = max(maxCount[0], len(path))

        for dr, dc in dirns:
            nr, nc = r + dr, c + dc
        
            # if out of bounds
            if not (0 <= nr < 10) or not (0 <= nc < 10): continue

            if (nr, nc) not in path and board[nr][nc] == "B":
                # and then if I can jump to here and backtrack
                landingRow, landingCol = r + 2*dr, c + 2*dc
                if ( 0 <= (landingRow) < 10) and ( 0 <= ( landingCol) < 10) and (board[landingRow][landingCol] == "." or  board[landingRow][landingCol] == "#"):
                
                    # mark this position
                    path.add( (nr, nc) )
                    board[nr][nc] = "."
                    backtrack(landingRow, landingCol)

                    #undo
                    path.remove( (nr, nc))
                    board[nr][nc] = "B"

    whitePositions = []

    for i in range(10):
        for j in range(10):
            if board[i][j] == "W":
                whitePositions.append( (i, j) )
        
    if not whitePositions: 
        print(0)
        continue
    path = set()
    # now we run a backtracking dfs on this board

    for whitePosition in whitePositions:


        # Clear the starting spot so it's a valid landing square later
        board[whitePosition[0]][whitePosition[1]] = '.'
        backtrack( whitePosition[0], whitePosition[1] )
        board[whitePosition[0]][whitePosition[1]] = 'W'


    print(maxCount[0])

    maxCount[0] = 0

"""

reflections on bugs:

incorrect landing ending position, was using only the index adjusted by 1

didnt realize you could have multiple white squares, which is why you also need
to mark it as white, and then move on

reading the input correctly, to handle the first whitespace

"""