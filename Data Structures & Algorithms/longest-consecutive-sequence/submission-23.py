class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elemset = set(nums)
        res = 0

        for num in nums:
            if num-1 in elemset:
                continue
            
            #this is the start of a sequence
            currval = num
            seqlen = 0
            while currval in elemset:
                currval += 1
                seqlen += 1
            res = max(res,seqlen)
        return res
            