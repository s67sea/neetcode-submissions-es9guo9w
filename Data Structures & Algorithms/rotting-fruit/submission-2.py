from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        numFresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numFresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        time = 0
        while q and numFresh > 0:
            qlen = len(q)
            for i in range(qlen):
                r,c = q.popleft()
                for i in range(4):
                    newr = r+dr[i]; newc = c+dc[i]
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc]==1:
                        grid[newr][newc] = 2
                        numFresh -= 1
                        q.append((newr,newc))
            time += 1
        
        if numFresh > 0:
            return -1
        return time
        