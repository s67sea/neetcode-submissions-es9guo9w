class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [0]*n
        for i in range(n):
            board[i] = ["."] * n

        def valid(row,col):
            if board[row][col] != ".":
                return False
            for i in range(n):
                if board[row][i] == "Q" or board[i][col] == "Q":
                    return False
            trow = row-1; tcol = col-1
            while trow>=0 and tcol>=0:
                if board[trow][tcol] == "Q": return False
                trow -=1; tcol -= 1
            trow = row+1; tcol = col-1
            while trow<n and tcol>=0:
                if board[trow][tcol] == "Q": return False
                trow +=1; tcol -= 1
            trow = row-1; tcol = col+1
            while trow>=0 and tcol<n:
                if board[trow][tcol] == "Q": return False
                trow -=1; tcol += 1
            trow = row+1; tcol = col+1
            while trow<n and tcol<n:
                if board[trow][tcol] == "Q": return False
                trow +=1; tcol += 1
            
            return True
        
        def dfs(row):
            #base case
            if row == n:
                boardcopy = [0] * n
                for i in range(n):
                    boardcopy[i] = "".join(board[i])
                res.append(boardcopy)
                return

            #recursive case
            for col in range(n):
                if valid(row,col):
                    board[row][col] = "Q"
                    dfs(row+1)
                    board[row][col] = "."
        
        dfs(0)
        return res