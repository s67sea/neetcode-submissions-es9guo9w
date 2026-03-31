class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        freqs = {}
        for elem in nums:
            if elem in freqs.keys():
                freqs[elem]+=1
            else:
                freqs[elem]=1
        
        buckets = [0]*(N+1) #bucket[i] is the numbers of frequency i
        for i in range(N+1):
            buckets[i] = []
        for elem in freqs.keys():
            buckets[freqs[elem]].append(elem)
        
        count = 0
        ret = []
        for i in range(N,-1,-1):
            count += len(buckets[i])
            for elem in buckets[i]:
                ret.append(elem)
            if count >= k:
                break
        return ret



