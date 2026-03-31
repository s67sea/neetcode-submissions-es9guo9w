class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return sum([nums.count(x) > 1 for x in nums]) > 0