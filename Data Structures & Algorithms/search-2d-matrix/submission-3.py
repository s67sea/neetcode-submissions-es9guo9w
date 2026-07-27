class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def getrc(index,m,n):
            #say for example you have a 5 by 4 matrix and entry 12
            #then 12 is the 2nd element in row 3
            r = index // n
            c = index % n
            return r,c

        #we can always convert num to location

        m = len(matrix)
        n = len(matrix[0])
        size = m*n

        leftptr = 0
        rightptr = size-1

        while leftptr <= rightptr:
            midpoint = (leftptr + rightptr)//2
            r,c = getrc(midpoint,m,n)
            val = matrix[r][c]

            if val == target:
                return True
            if val < target:
                #too small, need to move up to top half
                leftptr = midpoint + 1
            if val > target:
                #too big, need to move down to bottom half
                rightptr = midpoint - 1
        
        return False


