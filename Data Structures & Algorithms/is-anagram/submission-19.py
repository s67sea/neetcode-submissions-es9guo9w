class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        for ch in s:
            if ch not in freqs: freqs[ch] = 0
            freqs[ch] += 1

        freqt = {}
        for ch in t:
            if ch not in freqt: freqt[ch] = 0
            freqt[ch] += 1
        
        return freqs == freqt