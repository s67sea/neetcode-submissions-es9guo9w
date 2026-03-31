import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # loc = bisect.bisect_left(nums,target)
        # if loc<len(nums) and nums[loc]==target:
        #     return loc
        # return -1

        left = 0; right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1