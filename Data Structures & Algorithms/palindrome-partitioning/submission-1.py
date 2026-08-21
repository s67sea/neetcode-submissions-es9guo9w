class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)

        res = []
        combo = []
        
        def dfs(i,seqstart,lastaccounted):
            if i == N:
                if lastaccounted == N-1:
                    res.append(combo.copy())
                return
            
            #if the current sequence is a palindrome we can split it off
            if s[seqstart:i+1][::-1] == s[seqstart:i+1]:
                combo.append(s[seqstart:i+1])
                dfs(i+1,i+1,i)
                combo.pop()

            #or we can always not split it off
            dfs(i+1,seqstart,lastaccounted)

        dfs(0,0,-1)
        return res