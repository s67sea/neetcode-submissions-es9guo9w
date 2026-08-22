class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #approach: mark all the non-surrounded O's with #'s
        #afterwards, iterate through. capture all remaining O's (turn into X's) while replacing #'s (non-captured) back to O's

        ROWS = len(board)
        COLS = len(board[0])
        dr = [0,0,-1,1]
        dc = [1,-1,0,0]

        def dfs(r,c):
            for i in range(4):
                newr = r+dr[i]; newc = c+dc[i]
                if 0<=newr<ROWS and 0<=newc<COLS and board[newr][newc]=="O":
                    board[newr][newc] = "#"
                    dfs(newr,newc)
        
        for r in range(ROWS):
            if board[r][0] == "O":
                board[r][0] = "#"
                dfs(r,0)

            if board[r][COLS-1] == "O":
                board[r][COLS-1] = "#"
                dfs(r,COLS-1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                board[0][c] = "#"
                dfs(0,c)
            if board[ROWS-1][c] == "O":
                board[ROWS-1][c] = "#"
                dfs(ROWS-1,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
