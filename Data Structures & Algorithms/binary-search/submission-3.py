import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        loc = bisect.bisect_left(nums,target)
        if loc<len(nums) and nums[loc]==target:
            return loc
        return -1