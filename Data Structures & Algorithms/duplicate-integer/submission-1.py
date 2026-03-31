class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return sum([nums.count(x) for x in nums]) > len(nums)