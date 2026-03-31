class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #an anagram is that which has the same frequency signature
        #build a dictionary where the frequency signature is the key
        #and the value is the list of strings

        hm = {}
        for word in strs:
            word = word.lower()

            signature = [0]*26
            for letter in word:
                signature[ord(letter)-ord('a')]+=1
            
            signature = tuple(signature)
            if signature in hm.keys():
                hm[signature].append(word)
            else:
                hm[signature] = [word]
        
        return list(hm.values())