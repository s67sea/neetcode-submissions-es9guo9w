class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This solution takes O(N) time and O(1) space
        N = len(nums)

        res = [1] * N

        prefix = 1
        for i in range(1,N):
            prefix *= nums[i-1]
            res[i] = prefix
        
        postfix = 1
        for i in range(N-2,-1,-1):
            postfix *= nums[i+1]
            res[i] *= postfix
        
        return res