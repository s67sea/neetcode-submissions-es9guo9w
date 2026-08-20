class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        combo = ""

        def dfs(numOpen, numClosed):
            nonlocal combo

            if len(combo) == 2*n:
                res.append(combo)
                return
            
            #if numClosed < numOpen then you are allowed to close. you can never have more closed than open
            if numClosed < numOpen:
                combo += ")"
                dfs(numOpen,numClosed+1)
                combo = combo[:-1]

            #if numOpen < budget(n) then you are allowed to open
            if numOpen < n:
                combo += "("
                dfs(numOpen+1,numClosed)
                combo = combo[:-1]
        
        dfs(0,0)
        return res