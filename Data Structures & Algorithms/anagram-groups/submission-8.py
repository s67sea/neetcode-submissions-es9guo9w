class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            freqs = [0]*26
            for elem in string:
                freqs[ord(elem)-ord('a')]+=1
            if tuple(freqs) in hashmap.keys():
                hashmap[tuple(freqs)].append(string)
            else:
                hashmap[tuple(freqs)] = [string]
        res = []
        for elem in hashmap.keys():
            res.append(hashmap[elem])
        return res