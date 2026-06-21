class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for sent in strs:
            sent = sent.lower()
            freqsent = [0] * 26
            for letter in sent:
                freqsent[ord(letter)-ord('a')] += 1
            if tuple(freqsent) not in res: res[tuple(freqsent)] = []
            res[tuple(freqsent)].append(sent)
        
        return list(res.values())