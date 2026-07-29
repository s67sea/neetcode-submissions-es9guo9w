class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #keep looking for j
       #use a set to keep track of what you've seen, since set operations are O(1)


        seen = {}
        for i, num in enumerate(nums):
            want = target - num
            if want in seen:
                return [seen[want],i]
            seen[num] = i
        return []
 

