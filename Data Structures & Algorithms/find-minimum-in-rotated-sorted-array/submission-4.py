class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        leftptr = 0
        rightptr = n-1

        while leftptr < rightptr:
            midpoint = (leftptr + rightptr) // 2
            
            if nums[midpoint] > nums[rightptr]:
                #min val is in the right half
                leftptr = midpoint + 1
            else:
                #min val is in the left half, but it could be the midpoint
                rightptr = midpoint
            
        return nums[leftptr] #could return rightptr as well, doesn't matter; they're the same value


            

