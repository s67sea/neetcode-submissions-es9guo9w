class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(c):
            if '0' <= c <= '9' or 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                return True
            return False
        
        left = 0; right = len(s)-1
        while left < right:
            if not isAlpha(s[left]):
                left += 1
            elif not isAlpha(s[right]):
                right -= 1
            else:
                #both left, right are alphanumeric
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True