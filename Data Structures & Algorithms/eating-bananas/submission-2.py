class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right: #can't be <= because we have a right=midpoint
            midpoint = (left+right)//2 #current eating speed

            time = 0
            for pilesize in piles:
                time += math.ceil(pilesize/midpoint)
            
            if time > h:
                #speed too slow
                left = midpoint + 1
            else:
                #speed fast enough. maybe we can try a smaller speed
                right = midpoint
            
        return left


