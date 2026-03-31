class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for elem in s:
            if elem in ['(','{','[']:
                stack.append(elem)
            else:
                if len(stack)==0: return False
                ret = stack.pop()
                if ret == '(' and elem != ')' or ret == '{' and elem != '}' or ret == '[' and elem != ']':
                    return False
        if len(stack) > 0:
            return False
        return True