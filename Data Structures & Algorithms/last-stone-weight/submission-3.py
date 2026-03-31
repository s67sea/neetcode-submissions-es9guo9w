import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones)==1:
            return stones[0]

        q = [-x for x in stones]
        heapq.heapify(q)

        while len(q)>1:
            #at least 2 remaining, make them fight
            x = heapq.heappop(q)
            y = heapq.heappop(q)
            x *= -1; y *= -1
            print(x,y)
            survivor = max(x-y,y-x)
            print(survivor)
            if survivor!=0:
                heapq.heappush(q,-survivor)
        
        if q:
            return -heapq.heappop(q)
        return 0 #no stone remaining