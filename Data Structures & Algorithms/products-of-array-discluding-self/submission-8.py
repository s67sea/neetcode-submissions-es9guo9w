class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [0]*N #left[i] = prod 0->i-1
        right = [0]*N #right[i] = prod n-10->i+!
        left[0] = right[N-1] = 1
        for i in range(1,N):
            left[i] = left[i-1] * nums[i-1]
        for i in range(N-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        
        res = [0]*N
        for i in range(N):
            res[i] = left[i] * right[i]
        return res
