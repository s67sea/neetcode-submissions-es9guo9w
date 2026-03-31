class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for elem in s:
            if elem in ['(','[','{']:
                stack.append(elem)
            elif not stack:
                return False
            elif elem == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            
            elif elem == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            
            elif elem == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0