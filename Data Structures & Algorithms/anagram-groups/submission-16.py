class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for string in strs:
            signature = [0]*26
            for c in string:
                signature[ord(c)-ord('a')] += 1
            output[tuple(signature)].append(string)
        
        return list(output.values())