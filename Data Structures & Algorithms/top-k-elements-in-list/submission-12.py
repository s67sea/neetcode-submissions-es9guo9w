class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency of each element ranges from 1 to n
        #first get the frequency of each element, then invert it
        #then take the top k

        n = len(nums)

        freqs = {}
        for i, num in enumerate(nums):
            if num in freqs.keys():
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        freqbuckets = [0]*n
        for i in range(n):
            freqbuckets[i] = []
        for index in freqs.keys():
            freqbuckets[freqs[index]-1].append(index)

        res = []
        index = n-1
        while k > 0:
            res += freqbuckets[index]
            k -= len(freqbuckets[index])
            index -= 1
        
        return res

