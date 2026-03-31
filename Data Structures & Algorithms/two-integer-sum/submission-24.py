class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,elem in enumerate(nums):
            hashmap[elem] = i
        for j in range(len(nums)):
            diff = target-nums[j]
            if diff in hashmap.keys() and hashmap[diff]!=j:
                return [j,hashmap[diff]]