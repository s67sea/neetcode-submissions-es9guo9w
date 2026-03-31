class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set) #row: values in the row as a set
        squares = defaultdict(set) #key is (r//3,c//3)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".": 
                    continue
                
                #actuall has a value in it
                if board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

                #it's in square r//3, c//3
                if board[r][c] in squares[(r//3,c//3)]:
                    return False
                squares[(r//3,c//3)].add(board[r][c])
        return True

