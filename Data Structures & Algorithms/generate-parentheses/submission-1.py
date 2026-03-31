class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def compute(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                compute(opened+1,closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                compute(opened,closed+1)
                stack.pop()
        compute(0,0)
        return res
