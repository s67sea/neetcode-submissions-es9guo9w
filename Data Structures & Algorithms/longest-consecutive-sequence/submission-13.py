class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #settify for O(1) lookup
        nums = set(nums)
        maxsubseq = 0
        for elem in nums:
            if elem-1 in nums:
                #not a seq start
                continue
            #seq start, keep looking as much as possible
            subseq = 0
            curr = elem
            while curr in nums:
                subseq += 1
                curr += 1
            maxsubseq = max(subseq,maxsubseq)
        return maxsubseq

            

