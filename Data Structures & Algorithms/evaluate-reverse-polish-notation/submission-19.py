class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token=='+':
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1 + elem2)
            elif token=='-':
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1 - elem2)
            elif token=='*':
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(elem1 * elem2)
            elif token=='/':
                elem2 = stack.pop()
                elem1 = stack.pop()
                stack.append(int(elem1 / elem2))
            else:
                stack.append(int(token))
        
        return int(stack[-1])