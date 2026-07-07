from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        #no freq is greater then n

        freqs = defaultdict(int) #val : freq
        for i, num in enumerate(nums):
            freqs[num] += 1
        
        #invert
        invfreq = defaultdict(list)
        for elem in freqs: #elem is the value
            invfreq[freqs[elem]].append(elem)

        res = []
        currfreq = n
        while k > 0:
            num_to_add = len(invfreq[currfreq])
            res += invfreq[currfreq]
            currfreq -= 1
            k -= num_to_add
        
        return res

