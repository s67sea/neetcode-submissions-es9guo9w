from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freqt = defaultdict(int)
        for ch in t:
            freqt[ch] += 1

        res = 100000000
        resstr = ""
        need = len(t) #how many chars left until we satisfy the reqs
        
        lhs = 0 #decrease this when we find smth valid
        rhs = 0 #increase this to get more valid things
        freqs = defaultdict(int)
        while rhs < len(s):
            #add the current rhs until we get something valid
            while need > 0 and rhs < len(s):
                freqs[s[rhs]] += 1
                if freqs[s[rhs]] <= freqt[s[rhs]]:
                    need -= 1
                rhs += 1
            if need > 0: break
            #update the left boundary as much as we can
            while need == 0:
                if rhs-lhs<res:
                    res=rhs-lhs
                    resstr = s[lhs:rhs]

                freqs[s[lhs]] -= 1
                if freqs[s[lhs]] < freqt[s[lhs]]:
                    need += 1
                lhs += 1
        return resstr

            
