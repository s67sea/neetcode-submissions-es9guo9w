class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        combo = []
        used = [False] * N

        def dfs():
            if len(combo) == N:
                res.append(combo.copy())
                return 
            
            for i in range(N):
                if not used[i]:
                    combo.append(nums[i])
                    used[i] = True
                    dfs()
                    combo.pop()
                    used[i] = False
        
        dfs()
        return res