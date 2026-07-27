class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftptr = 0
        rightptr = len(numbers) - 1

        while leftptr < rightptr:
            #check the status if its too high or too low
            currsum = numbers[leftptr] + numbers[rightptr]
            if currsum < target:
                leftptr += 1
            if currsum > target:
                rightptr -= 1
            if currsum == target:
                return [leftptr+1,rightptr+1]
        
        return None