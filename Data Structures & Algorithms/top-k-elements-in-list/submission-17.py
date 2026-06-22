import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {} #num: freq
        for num in nums:
            if num not in freqs: freqs[num] = 0
            freqs[num] += 1
        
        q = []
        for key in freqs:
            heapq.heappush(q,(freqs[key],key))
            if len(q) > k:
                heapq.heappop(q)

        return [num for freq,num in q]

        