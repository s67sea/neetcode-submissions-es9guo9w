class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stack just to store the addends
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == "+":
                    res = op2 + op1
                elif token == "-":
                    res = op2 - op1
                elif token == "*":
                    res = op2 * op1
                elif token == "/":
                    res = int(op2 / op1)
                stack.append(res)
        return stack.pop()