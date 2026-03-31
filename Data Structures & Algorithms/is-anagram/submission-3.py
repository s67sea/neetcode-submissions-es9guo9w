class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqs = {}
        freqt = {}
        for l in s:
            if l not in freqs.keys():
                freqs[l] = 1
            else:
                freqs[l] += 1
        for l in t:
            if l not in freqt.keys():
                freqt[l] = 1
            else:
                freqt[l] += 1
        return freqs == freqt
