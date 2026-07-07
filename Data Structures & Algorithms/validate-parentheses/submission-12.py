class Solution:
    def isValid(self, s: str) -> bool:
        #make a stack
        #put opening braces on the stack
        #for closing braces pop the stack and make sure they line up
        #this forces the closing order to match the opening order

        pairs = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        stack = []
        for el in s:
            if el in pairs:
                stack.append(el)
            elif stack:
                top = stack.pop()
                if pairs[top] != el:
                    return False
            else:
                return False
        
        return len(stack) == 0
                