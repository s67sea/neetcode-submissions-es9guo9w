class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0; right = len(numbers)-1
        currsum = numbers[left] + numbers[right]
        while left < right:
            if currsum > target:
                right -= 1
                currsum = numbers[left] + numbers[right]
            elif currsum < target:
                left += 1
                currsum = numbers[left] + numbers[right]
            else:
                return [left+1,right+1]
        return []
        