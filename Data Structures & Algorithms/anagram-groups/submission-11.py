class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            #construct freq array
            freq = [0]*26
            for el in s:
                freq[ord(el)-ord('a')]+= 1
            hm[tuple(freq)].append(s)
        
        return [l for l in hm.values()]
            