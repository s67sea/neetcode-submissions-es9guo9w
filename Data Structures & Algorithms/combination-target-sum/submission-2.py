class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []

        def dfs(curr, minindex):
            if curr == target:
                res.append(combo.copy())
                return
            if curr > target:
                return
            for i in range(minindex,len(nums)):
                combo.append(nums[i])
                dfs(curr+nums[i],i)
                combo.pop()

        
        dfs(0,0)
        return res
            

            
