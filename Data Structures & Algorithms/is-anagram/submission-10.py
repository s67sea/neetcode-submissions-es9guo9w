class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        for elem in s:
            if elem not in freqs.keys(): freqs[elem] = 0
            freqs[elem] += 1

        freqt = {}
        for elem in t:
            if elem not in freqt.keys(): freqt[elem] = 0
            freqt[elem] += 1
         
        return freqs == freqt