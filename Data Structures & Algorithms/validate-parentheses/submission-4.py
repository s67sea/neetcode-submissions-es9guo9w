class Solution:
    def isValid(self, s: str) -> bool:
        #stack has the opens, close need to match the opens
        stack = []
        hm = {"{":"}","[":"]","(":")"}#open:close
        for ch in s:
            if ch in hm.keys():
                #open parenthesis
                stack.append(ch)
            else:
                #close parenthesis
                if not stack: 
                    return False
                if ch != hm[stack.pop()]:
                    return False
        if stack: 
            return False
        return True