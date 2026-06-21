class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #number : index

        for i, num in enumerate(nums):
            want = target - num
            if want in seen and seen[want]!=i:
                return [seen[want],i]
            seen[num] = i
        
        return []
