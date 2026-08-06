import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #we'll do the heap version which is O(n log n), since heap operations are O(log n)
        q = []
        res = []

        for i in range(k):
            heapq.heappush(q,(-nums[i],i))
        while i < len(nums):
            heapq.heappush(q,(-nums[i],i))
            while q[0][1] < (i-k+1):
                heapq.heappop(q)
            #while the "maximum" is out of range
            #append the legit maximum to the output
            res.append(-q[0][0])
            i += 1
        
        return res