class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0; right = len(numbers)-1
        while left < right:
            #compute currsum
            currsum = numbers[left]+numbers[right]
            if currsum < target:
                #too low, need to move the left pointer up
                left += 1
            elif currsum > target:
                #too high, need to move the right pointer down
                right -= 1
            else:
                #exactly equal
                return [left+1,right+1]
        return []