class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        leftptr = 0
        rightptr = n - 1

        maxarea = 0

        while leftptr < rightptr:
            currarea = (rightptr - leftptr) * min(heights[leftptr],heights[rightptr])
            maxarea = max(maxarea,currarea)

            if heights[leftptr] < heights[rightptr]:
                leftptr += 1
            else:
                rightptr -= 1
            
        return maxarea