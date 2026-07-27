class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftptr = 0
        rightptr = len(s) - 1
        s = s.lower()

        while leftptr <= rightptr:
            while leftptr < rightptr and not s[leftptr].isalnum():
                leftptr += 1
            while leftptr < rightptr and not s[rightptr].isalnum():
                rightptr -= 1

            if s[leftptr] != s[rightptr]:
                return False
            leftptr += 1
            rightptr -= 1
        
        return True