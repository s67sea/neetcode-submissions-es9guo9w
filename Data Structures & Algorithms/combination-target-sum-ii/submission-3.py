class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sort the numbers. if they're sorted then duplicates are next to each other
        #the "valid" range will not include the current number
        #if you skip a number you must skip all other instances of the number
        candidates.sort()

        res = []
        combo = []

        def dfs(curr,start):
            if curr == target:
                res.append(combo.copy())
                return
            if curr > target:
                return
            
            # curr < target
            for i in range(start,len(candidates)):
                if i>0 and i>start and candidates[i]==candidates[i-1]:
                    #you don't get to add a duplicated number unless it's the first-ever option
                    #that way duplication happens only once per uniq elem
                    continue
                if candidates[i]+curr > target:
                    break
                
                combo.append(candidates[i])
                dfs(curr+candidates[i],i+1)
                combo.pop()
            
        dfs(0,0)
        return res