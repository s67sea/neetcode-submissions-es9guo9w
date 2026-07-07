class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        #prefix[i] = prod for prefix[0...i-1]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1] * n
        #suffix[i] = prod for suffix[i+1...n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        return [prefix[i]*suffix[i] for i in range(n)]
        