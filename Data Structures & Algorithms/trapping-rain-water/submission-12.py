class Solution:
    def trap(self, height: List[int]) -> int:
        #if we're at posn i, let l be highest left, r highest right
        #w[i] = min(h[l],h[r]) - h[i]

        #the following is a good solution but takes O(N) space in add'n to O(N) time
        # n = len(height)

        # lefts = [0] * n #max height leftwards including i
        # rights = [0] * n #max height rightwards including i

        # lefts[0] = height[0]
        # rights[n-1] = height[n-1]

        # for i in range(1,n):
        #     lefts[i] = max(lefts[i-1],height[i])
        # for i in range(n-2,-1,-1):
        #     rights[i] = max(rights[i+1],height[i])
        
        # res = 0
        # for i in range(1,n-1):
        #     res += max(min(lefts[i-1],rights[i+1]) - height[i],0)
        
        # return res

        #Now we attempt a solution that takes O(1) space

        #We use a 2 pointer approach. And we actually compute AT the boundary
        #Progress the pointer on the lower side bc the higher wall can't save it
        n = len(height)
        leftptr = 1
        rightptr = n-2

        leftmax = height[0]
        rightmax = height[n-1]

        res = 0

        while leftptr <= rightptr:
            if leftmax <= rightmax:
                #the wall on the left is shorter
                #this means that no matter where the true right wall is, the height for this particular value is capped by the left wall
                res += max(leftmax - height[leftptr],0)
                leftmax = max(leftmax,height[leftptr])
                leftptr += 1

            else:
                res += max(rightmax - height[rightptr],0)
                rightmax = max(rightmax,height[rightptr])
                rightptr -= 1
        
        return res
                
