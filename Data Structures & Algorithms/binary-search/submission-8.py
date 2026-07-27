class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftptr = 0
        rightptr = len(nums)-1

        while leftptr <= rightptr:
            midpoint = (leftptr + rightptr)//2 
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                #too small so it's in the upper half
                leftptr = midpoint + 1
            elif nums[midpoint] > target:
                #too big so it's in the lower half
                rightptr = midpoint - 1
        
        return -1