class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0; right = len(heights)-1

        maxamt = 0

        while left < right:
            amt = (right-left)*min(heights[right],heights[left])
            maxamt = max(maxamt,amt)
            #move the goalpost of the shorter one
            if heights[left]<=heights[right]:
                left += 1
            else:
                right -= 1
        return maxamt
