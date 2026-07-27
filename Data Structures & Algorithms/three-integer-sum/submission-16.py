class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []

        for i in range(n-2):
            #if its sorted i should be negative
            if nums[i] > 0: break

            #don't repeat input i value
            if i>0 and nums[i] == nums[i-1]: continue

            a = nums[i] #let this be the first number
            #now we need to find b,c in the range (i+1,n)
            #that add up to -a
            target = -1*a

            leftptr = i+1
            rightptr = n-1

            while leftptr < rightptr:
                currsum = nums[leftptr] + nums[rightptr]

                if currsum < target:
                    leftptr += 1
                if currsum > target:
                    rightptr -= 1
                if currsum == target:
                    res.append((nums[i],nums[leftptr],nums[rightptr]))

                    leftptr += 1
                    rightptr -= 1

                    #skip duplicate values of leftptr
                    while leftptr < rightptr and nums[leftptr] == nums[leftptr-1]:
                        leftptr += 1

                    #skip duplicate values of rightptr
                    while leftptr < rightptr and nums[rightptr] == nums[rightptr+1]:
                        rightptr -= 1
                
        return res
