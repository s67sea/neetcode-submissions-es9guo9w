class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #should have the same frequency signature
        freqs = [0]*26
        for el in s:
            freqs[ord(el)-ord('a')]+=1


        freqt = [0]*26
        for el in t:
            freqt[ord(el)-ord('a')]+=1
        
        return freqs==freqt