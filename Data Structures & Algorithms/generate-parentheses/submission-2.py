class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def compute(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n: #we can always open a bracket
                stack.append("(")
                compute(opened+1,closed)
                stack.pop()
            if closed < opened: #less closed than opened means it's valid to close a bracket
                stack.append(")")
                compute(opened,closed+1)
                stack.pop()
        compute(0,0)
        return res
