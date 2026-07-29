from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
        
        freqs = defaultdict(int)
        for ch in s:
            freqs[ch] += 1
        
        freqt = defaultdict(int)
        for ch in t:
            freqt[ch] += 1
        
        return freqs == freqt
