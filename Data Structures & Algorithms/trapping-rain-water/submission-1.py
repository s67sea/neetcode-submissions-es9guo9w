class Solution:
    def trap(self, height: List[int]) -> int:
        #if we're at posn i, let l be highest left, r highest right
        #w[i] = min(h[l],h[r]) - h[i]
        n = len(height)

        lefts = [0] * n
        rights = [0] * n

        lefts[0] = height[0]
        rights[n-1] = height[n-1]

        for i in range(1,n):
            lefts[i] = max(lefts[i-1],height[i])
        for i in range(n-2,-1,-1):
            rights[i] = max(rights[i+1],height[i])
        
        res = 0
        for i in range(1,n-1):
            res += max(min(lefts[i-1],rights[i+1]) - height[i],0)
        
        return res