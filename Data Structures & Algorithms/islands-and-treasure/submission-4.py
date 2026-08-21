from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        #add all of the treasure chests to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]

        #process levels
        level = 0
        while q:
            qlen = len(q)
            for i in range(qlen):
                r,c = q.popleft()
                for i in range(4):
                    newr = r+dr[i]; newc = c+dc[i]
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc]==INF:
                        q.append((newr,newc))
                        grid[newr][newc] = level + 1
            level += 1


        
