class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]

        ROWS = len(heights)
        COLS = len(heights[0])

        accessible_pac = [[False]*COLS for i in range(ROWS)]
        accessible_atl = [[False]*COLS for i in range(ROWS)]
        
        def dfs(r,c,accessible_src):
            if accessible_src[r][c]:
                return
            
            #this node is accessible
            accessible_src[r][c] = True

            for i in range(4):
                newr = r+dr[i]; newc = c+dc[i]
                if 0<=newr<ROWS and 0<=newc<COLS and heights[newr][newc]>=heights[r][c]:
                    dfs(newr,newc,accessible_src)

        for r in range(ROWS):
            dfs(r,0,accessible_pac)
            dfs(r,COLS-1,accessible_atl)
            
        for c in range(COLS):
            dfs(0,c,accessible_pac)
            dfs(ROWS-1,c,accessible_atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if accessible_pac[r][c] and accessible_atl[r][c]:
                    res.append([r,c])
        
        return res
