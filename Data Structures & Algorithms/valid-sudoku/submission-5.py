class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(9):
            for testval in range(1,10):
                if board[i].count(str(testval)) > 1:
                    return False
        
        #check cols
        for i in range(9):
            #on column i
            freqs = {}
            for j in range(1,10):
                freqs[j] = 0
            
            for j in range(9):
                if board[j][i]!=".":
                    freqs[int(board[j][i])] += 1
            for val in freqs.values():
                if val > 1:
                    return False
        
        #check 3x3s
        for rowoffset in range(0,9,3):
            for coloffset in range(0,9,3):
                freqs = {}
                for i in range(1,10):
                    freqs[i] = 0

                for i in range(3):
                    for j in range(3):
                        if board[rowoffset+i][coloffset+j]!= ".":
                            freqs[int(board[rowoffset+i][coloffset+j])] += 1
                
                for val in freqs.values():
                    if val > 1:
                        return False
        
        return True
