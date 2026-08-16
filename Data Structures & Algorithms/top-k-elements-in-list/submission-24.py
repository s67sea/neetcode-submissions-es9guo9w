from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        for num in nums:
            freqmap[num] += 1
        
        invfreqmap = defaultdict(list) # freq : num
        for elem in freqmap:
            invfreqmap[freqmap[elem]].append(elem)
        
        res = []
        currfreq = len(nums)
        while currfreq > 0 and k > 0:
            #pass through the current maxfreq
            res += invfreqmap[currfreq]
            k -= len(invfreqmap[currfreq])
            currfreq -= 1
        
        return res
            