class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(currString,numOpen,numClosed):
            nonlocal res, n
            if len(currString) == 2*n:
                res.append(currString)
                return
            if numOpen < n:
                recurse(currString+"(",numOpen+1,numClosed)
            if numClosed < numOpen:
                recurse(currString+")",numOpen,numClosed+1)
        
        recurse("",0,0)
        return res
            