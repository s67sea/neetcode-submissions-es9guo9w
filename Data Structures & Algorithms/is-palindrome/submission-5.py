class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(ch):
            if '0'<=ch<='9' or 'a'<=ch<='z' or 'A'<=ch<='Z':
                return True
            return False

        left = 0; right = len(s)-1
        while left < right:
            if not isAlpha(s[left]):
                left += 1
            elif not isAlpha(s[right]):
                right -= 1
            #now both are alpha
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True        