from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use the freqlist tuple as an index into a hashmap
        #then convert the values to list at the end

        groups = defaultdict(list)
        for word in strs: 
            word = word.lower()
            freqlist = [0] * 26
            for ch in word:
                freqlist[ord(ch) - ord('a')] += 1
            groups[tuple(freqlist)].append(word)
        
        return list(groups.values())
