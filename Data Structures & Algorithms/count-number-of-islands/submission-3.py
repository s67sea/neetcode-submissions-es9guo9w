class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #directions
        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return
            if grid[r][c]== "0":
                return
            
            grid[r][c] = "0"
            
            dr = [0,0,-1,1]
            dc = [-1,1,0,0]

            for i in range(4):
                dfs(r+dr[i],c+dc[i])
            
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    dfs(r,c)
                    res += 1
        return res
        
                    
