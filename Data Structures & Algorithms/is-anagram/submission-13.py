class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram = same frequency signature
        s = s.lower()
        t = t.lower()

        freqs = defaultdict(int)
        freqt = defaultdict(int)

        for elem in s:
            freqs[ord(elem)-ord('a')] += 1

        for elem in t:
            freqt[ord(elem)-ord('a')] += 1
        
        return freqs == freqt