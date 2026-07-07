class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #you can move the elems to a set for O(1) lookup
        #not every element is a potential start of sequence.
            # you are the start of seq if x in list
            # and x-1 not in list


        numset = set(nums)

        maxlen = 0

        for num in numset:
            if num-1 not in numset:
                #num is a potential start
                currlen = 1
                numcopy = num
                while numcopy+1 in numset:
                    currlen += 1
                    numcopy += 1
                maxlen = max(maxlen, currlen)
        
        return maxlen

#each number is processed only by either the while loop or the outerloop as a start, not by both. so it's O(N)


