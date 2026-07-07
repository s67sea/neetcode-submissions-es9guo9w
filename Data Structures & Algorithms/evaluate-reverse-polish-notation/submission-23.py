class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                match token:
                    case "+":
                        stack.append(op1+op2)
                    case "-":
                        stack.append(op1-op2)
                    case "*":
                        stack.append(op1*op2)
                    case _:
                        stack.append(int(op1/op2))
        
        return int(stack[0])
