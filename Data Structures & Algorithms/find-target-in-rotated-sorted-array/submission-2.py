class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the cut point
        #then binary search each sorted part to find the target

        n = len(nums)

        #1. find the cut point
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                #means that the drop off point is in the right half
                left = mid + 1
            else:
                #means that the drop off point is in the left half or the middle
                right = mid
        minval = nums[left]
        minindex = left

        #2. search the first half for the target
        left = 0
        right = max(minindex-1,0)
        while minindex > 0 and left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        #3. search the second half for the target
        left = minindex
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1