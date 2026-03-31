class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        #"new starts" are those where n-1 isn't in the set
        maxlength = 0
        for num in numset:
            if num-1 not in numset:
                #this is a valid start
                length = 0
                while num+length in numset:
                    length += 1
                maxlength = max(length,maxlength)
        return maxlength

