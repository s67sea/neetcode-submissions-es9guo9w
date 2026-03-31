class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagrams are the signature for the hashmap 
        hm = defaultdict(list)
        for s in strs:
            freq = [0]*26
            for el in s:
                freq[ord(el)-ord('a')]+=1
            hm[tuple(freq)].append(s)
        
        return list(hm.values())