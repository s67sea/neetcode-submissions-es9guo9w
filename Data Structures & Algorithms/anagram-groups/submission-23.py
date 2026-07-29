from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key: tuple of the anagram
        #value: word

        freqdict = defaultdict(list)

        for sent in strs:
            sent = sent.lower()

            freqs = [0]*26
            for s in sent:
                freqs[ord(s)-ord('a')] += 1
            freqdict[tuple(freqs)].append(sent)
        
        return list(freqdict.values())


