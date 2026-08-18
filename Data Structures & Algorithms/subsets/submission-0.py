class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i): #i is the number index to add
            if i >= len(nums):
                #we got to the end so this is a complete subset
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            dfs(i+1) # you can add the number
            subset.pop() #or you can not
            dfs(i+1) #either way you move on
        
        dfs(0)
        return res