class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            ret[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ret[i] *= postfix 
            postfix *= nums[i]
        return ret

        """
        ret = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j!=i:
                    prod *= nums[j]
            ret.append(prod)
        return ret
        """