class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0

        for num in nums:
            if num-1 in numset:
                continue
            streak = 1
            curr = num
            while curr+1 in numset:
                streak += 1
                curr += 1
            count = max(count, streak)
            
        return count