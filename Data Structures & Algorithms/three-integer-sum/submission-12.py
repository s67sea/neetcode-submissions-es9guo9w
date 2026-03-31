class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            # - nums[i] = nums[j] + nums[k] 
            target = -1 * nums[i]
            #find pairs of j,k (that aren't i) that sum to 0
            j = i+1; k = len(nums) - 1
            while j < k:
                currsum = nums[j] + nums[k]
                
                if currsum == target:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1;k-=1
                elif currsum > target:
                    k -=1
                elif currsum < target:
                    j += 1
                
        return list(list(e) for e in res)