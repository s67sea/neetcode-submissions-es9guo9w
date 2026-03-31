import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #maxheap, so store the negatives
        #heappop should kick out big values (i.e. very negative)
        q = []
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(q,(-dist,[x,y]))
            while len(q) > k:
                heapq.heappop(q)
        return [elem[1] for elem in q]
