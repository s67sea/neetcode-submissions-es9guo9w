class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        
        seencols = set() #ensure we haven't placed anything in this col yet
        seendiag1 = set() #entries in a given main diag has a consistent value for (row-col)
        seendiag2 = set() #entries in a given off diag has a consistent value for (row+col)

        
        def dfs(row):
            #base case
            if row == n:
                boardcopy = ["".join(row) for row in board]
                res.append(boardcopy)
                return

            #recursive case
            for col in range(n):
                if (col not in seencols) and ((row-col) not in seendiag1) and ((row+col) not in seendiag2): #check valid
                    board[row][col] = "Q"
                    seencols.add(col)
                    seendiag1.add(row-col)
                    seendiag2.add(row+col)
                    dfs(row+1)
                    board[row][col] = "."
                    seencols.remove(col)
                    seendiag1.remove(row-col)
                    seendiag2.remove(row+col)
        
        dfs(0)
        return res