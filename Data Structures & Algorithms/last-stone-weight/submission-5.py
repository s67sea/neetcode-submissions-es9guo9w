import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for wt in stones:
            heapq.heappush(q,-wt)
        
        while len(q) > 1:
            wt1 = -1 * heapq.heappop(q)
            wt2 = -1 * heapq.heappop(q)
            if wt1 != wt2:
                heapq.heappush(q,-1*abs(wt1-wt2)) 

        return -1*q[0] if q else 0
