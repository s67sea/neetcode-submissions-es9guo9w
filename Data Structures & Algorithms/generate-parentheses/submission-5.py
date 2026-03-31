class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def rec(opened,closed):
            #base case
            if opened==closed==n:
                res.append(''.join(stack))
                return
            
            if opened < n:
                #left open
                stack.append("(")
                rec(opened+1,closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                rec(opened,closed+1)
                stack.pop()
        rec(0,0)
        return res