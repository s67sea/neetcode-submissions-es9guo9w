class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,elem in enumerate(nums):
            hashmap[elem] = i
        for i,val in enumerate(nums):
            diff = target-val
            if diff in hashmap and hashmap[diff]!=i:
                return [i,hashmap[diff]]