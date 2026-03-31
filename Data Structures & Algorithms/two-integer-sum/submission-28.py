class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, elem in enumerate(nums):
            hm[elem] = i
        
        for i in range(len(nums)):
            curr = nums[i]
            want = target - curr 

            if want in hm.keys() and hm[want]!=i:
                return [min(i,hm[want]),max(i,hm[want])]
