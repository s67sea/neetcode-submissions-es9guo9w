class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqs = [0]*26
        freqt = [0]*26
        for l in s:
            freqs[ord(l)-97]+=1
        for l in t:
            freqt[ord(l)-97]+=1
        return freqs==freqt