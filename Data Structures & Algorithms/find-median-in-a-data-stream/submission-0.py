import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = [] #bottom half, use negatives of numbers
        self.minheap = [] #top half

    def addNum(self, num: int) -> None:
        #push the number onto the bottom half
        #bubble one number from bottom half onto top half
        #in this process bottom half size hasn't changed but top half size has increased by 1
        heapq.heappush(self.maxheap,-1*num)
        num = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap,-1*num)

        #if top half size is too big, bubble one back down to bottom half
        if len(self.minheap) - len(self.maxheap) > 1:
            num = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-1*num)
        

    def findMedian(self) -> float:
        #if top half bigger, then return the bottom of the top half
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]

        #if they're the same size take median
        return (self.minheap[0] + (-1*self.maxheap[0]))/2
        
        