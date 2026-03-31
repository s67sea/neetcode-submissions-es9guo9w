class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()

        freqs = {}
        for e in s:
            if e in freqs.keys():
                freqs[e] += 1
            else:
                freqs[e] = 1


        freqt = {}
        for e in t:
            if e in freqt.keys():
                freqt[e] += 1
            else:
                freqt[e] = 1
        
        return freqs == freqt