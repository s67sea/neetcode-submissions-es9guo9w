class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return 0
            if grid[r][c]==0:
                return 0
            
            dr = [0,0,-1,1]
            dc = [-1,1,0,0]

            grid[r][c] = 0
            islandsize = 1

            for i in range(4):
                islandsize += dfs(r+dr[i],c+dc[i])
            
            return islandsize
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    size = dfs(r,c)
                    res = max(res,size)
        return res

