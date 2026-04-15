class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):

                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue

                # place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                backtrack(row + 1)

                # undo
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        backtrack(0)
        return res
# rows: 0, 1, 2, ..., n-1
# 0, 1, 2, …, n-1   → n rows total
# so becauuse of 0 iindexed, if ireach row n, it means i filled n rows



# base case means:
# we successfully placed queens in rows:
# 0,1,2,3,4,5,6,7
# not necessaliry that we placed in any such and such columns - but i do record those column choices in the board i build up

# Problem	Choice type
# Subsets	include / exclude (2 options)
# N-Queens	pick a column (n options)
#  to clarify when i have row 0 as my starting, that means i have 8 chocies, and could choose col 0
        # res = []
        # currentSolution = [[["."] for _ in range(n)] for _ in range(n)]

        # column = set()
        # rowIndex = 0

        # diagonalPos = set()
        # diagonalNeg = set()

        # def helper(i):
        #     nonlocal rowIndex

        #     if queensPlaced == n:
        #     res.append(currentSolution)
        #     return

        #     # skip choices that violate constraints
        #     for c in range(n):
        #         if c in column:
        #             continue

        #     # make choice
        #     currentSolution[rowIndex ][i] = "Q"
        #     rowIndex += 1
        #     helper(i+1)

        #     # undo - below was wrong, as There is no “skip recursion” branch in N-Queens. so 
        #     rowIndex -= 1

        #     currentSolution[rowIndex ][i] = "."
        #     helper(i+1)

        # helper(0)
        # return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def helper(i):
            if i == len(nums):
                res.append(path.copy())
                return
  
            # choose
            path.append(nums[i])
            helper(i + 1)
            path.pop()

            # skip
            helper(i + 1)

        helper(0)
        return res