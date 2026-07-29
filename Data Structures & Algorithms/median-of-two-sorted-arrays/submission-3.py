class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsA = nums1
        numsB = nums2
        if len(nums1) > len(nums2):
            numsA = nums2
            numsB = nums1
        m = len(numsA)
        n = len(numsB)

        mini = 0
        maxi = len(numsA) 
        #i tells you how many elements to the left of i you pick from numsA

        while mini <= maxi:
            i = (mini + maxi) // 2 #this is the value of i
            j = (m+n)//2 - i
            if 0 <= j <= len(numsB):
                if i>0 and j<n and numsA[i-1] > numsB[j]:
                    #then the value of i must be too big
                    maxi = i-1
                elif j > 0 and i<m and numsB[j-1] > numsA[i]:
                    #then the value of i must be too small
                    mini = i+1
                else:
                    #we must be in a correct situation so we can compute the median
                    leftA = numsA[i-1] if i>0 else float("-inf")
                    leftB = numsB[j-1] if j>0 else float("-inf")
                    rightA = numsA[i] if i<m else float("inf")
                    rightB = numsB[j] if j<n else float("inf")

                    if (m+n)%2 == 1:
                        #odd number of elements
                        return min(rightA,rightB)
                    else:
                        return (
                            max(leftA,leftB) + min(rightA,rightB)
                        ) / 2