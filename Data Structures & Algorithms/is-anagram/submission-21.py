class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        for el in s:
            freqs[el] = freqs.get(el,0) + 1
        
        freqt = {}
        for el in t:
            freqt[el] = freqt.get(el,0) + 1

        return freqs == freqt