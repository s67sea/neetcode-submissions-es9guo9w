class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #indinv
        # indinv = {}
        # for i, num in enumerate(nums):
        #     indinv[num] = i
        
        # for i, num in enumerate(nums):
        #     want = target - num
        #     if want in indinv and indinv[want] != i:
        #         return [i, indinv[want]]

        seen = {}
        for i, num in enumerate(nums):
            want = target - num
            if want in seen and seen[want] != i:
                return [seen[want], i]
            seen[num] = i