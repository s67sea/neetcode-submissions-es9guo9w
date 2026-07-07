class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #go through rows
        for i in range(9): #row i
            seen = set()
            for j in range(9):
                if board[i][j] == ".": 
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        #go thru cols
        for j in range(9): #col j
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        #go through each cell
        for boxrow in range(3):
            for boxcol in range(3):
                #i = boxrow*3 + row
                #j = boxcol*3 + col
                seen = set()
                for row in range(3):
                    for col in range(3):
                        i = boxrow*3 + row
                        j = boxcol*3 + col
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        
        return True
