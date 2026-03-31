class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0; right = len(heights)-1
        maxarea = 0
        while left < right:
            area = min(heights[right],heights[left])*(right-left)
            maxarea = max(maxarea, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxarea