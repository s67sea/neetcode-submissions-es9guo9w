class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        res = [1] * N

        pref = [1] * N
        #add the lhs
        #traverse from left to right, res[i] contains product of res[0...i-1]
        for i in range(1,N):
            pref[i] = pref[i-1] * nums[i-1]

        post = [1] * N
        #now add the rhs
        #traverse from right to left, res[i] contains product of res[i+1...n-1]
        for i in range(N-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]
        
        for i in range(N):
            res[i] = pref[i] * post[i]
        
        return res
        

