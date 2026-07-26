class Solution:
    def isValid(self, s: str) -> bool:
        #make stack
        #opening braces go on stack
        #closing braces get checked against the stack pop (if items left)

        pairs = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        stack = []

        for elem in s:
            if elem in pairs:
                stack.append(elem)
            elif stack:
                if pairs[stack.pop()] != elem:
                    return False
            else:
                return False
        return not stack