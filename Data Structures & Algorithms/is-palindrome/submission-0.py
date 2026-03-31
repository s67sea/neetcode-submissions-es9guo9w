class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(c):
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
                return True
            return False
        
        lhs = 0
        rhs = len(s)-1

        while lhs < rhs:
            if not isAlpha(s[lhs]):
                lhs += 1
            elif not isAlpha(s[rhs]):
                rhs -= 1
            else:
                #both lhs, rhs are alpha
                if s[lhs].lower() != s[rhs].lower():
                    return False
                lhs += 1
                rhs -= 1
        return True