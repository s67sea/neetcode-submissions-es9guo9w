import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #minheap: elements, boot out the smallest one to keep topk
        q = []
        for elem in nums:
            heapq.heappush(q,elem)
            if len(q)>k:
                heapq.heappop(q)
        return q[0]
