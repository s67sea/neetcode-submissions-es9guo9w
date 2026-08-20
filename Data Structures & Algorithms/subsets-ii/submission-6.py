class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #this assums that equal numbers are adjacent
        nums.sort()
        
        N = len(nums)
        res = []
        combo = []

        def dfs(i):
            if i == N:
                res.append(combo.copy())
                return
            
            #you can either add the number or you can not. 
            #but if you choose not to add the number you have to skip all other copies of the number
            combo.append(nums[i])
            dfs(i+1)

            combo.pop()

            temp = i
            while i<N and nums[i]==nums[temp]:
                i += 1
            dfs(i)
        
        dfs(0)
        return res