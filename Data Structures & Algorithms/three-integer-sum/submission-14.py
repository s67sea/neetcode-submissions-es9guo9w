class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #fix i, look for j and k in a sorted list
        nums.sort()

        triplets = set()
        for i in range(len(nums)):
            #fix i
            target = -1*nums[i]

            #find j, k to do this
            j=i+1; k=len(nums)-1
            while j < k:
                currsum = nums[j]+nums[k]
                if currsum==target:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j += 1; k -= 1
                elif currsum < target:
                    #too low, need to move left pointer up
                    j += 1
                else:
                    #too high, need to move right pointer down
                    k -= 1
        return list(list(el) for el in triplets)
