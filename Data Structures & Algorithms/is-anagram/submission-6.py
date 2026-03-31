class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        freqS = [0]*26
        for elem in s:
            freqS[ord(elem)-ord('a')]+=1
        freqT = [0]*26
        for elem in t:
            freqT[ord(elem)-ord('a')]+=1
        return freqS == freqT