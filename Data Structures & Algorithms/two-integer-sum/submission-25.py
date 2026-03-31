class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #easy lookup with location: hashmap
        hm = {}
        for i, el in enumerate(nums):
            hm[el]=i
        
        for i in range(len(nums)):
            curr = nums[i]
            want = target-curr

            if want in hm and hm[want]!=i:
                first = min(hm[want],i)
                second = max(hm[want],i)
                return [first,second]