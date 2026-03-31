class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #build a frequency map: O(N)
        freqs = defaultdict(int)
        for num in nums:
            freqs[num]+=1

        #freqs are all between 1 and n
        N = len(nums)
        buckets = [0]*(N+1) #bucket[i] is the one with freq i
        for i in range(N+1):
            buckets[i] = []
        for num,freq in freqs.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(N,-1,-1):
            res += buckets[i]
            k -= len(buckets[i])
            if k==0:
                break
        return res

