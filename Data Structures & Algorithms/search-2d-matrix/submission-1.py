import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix); cols = len(matrix[0])
        left = 0; right = rows-1
        corrRow = -1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                corrRow =  mid
                break
            elif matrix[mid][0] > target:
                right = mid-1
            elif matrix[mid][-1] < target:
                left = mid+1
        if corrRow == -1:
            return False
        
        #now we need to search this row
        row = matrix[corrRow]
        left = 0; right=cols-1
        while left <= right:
            mid = (left+right)//2
            if row[mid]==target:
                return True
            elif row[mid]>target:
                right = mid-1
            elif row[mid]<target:
                left = mid+1
        return False