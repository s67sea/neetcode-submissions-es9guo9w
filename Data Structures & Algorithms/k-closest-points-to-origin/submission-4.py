import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for [x,y] in points:
            dist = x**2 + y**2
            heapq.heappush(q,(-1*dist,x,y))
        
        while len(q) > k:
            heapq.heappop(q)
        
        return [[x,y] for dist,x,y in q]