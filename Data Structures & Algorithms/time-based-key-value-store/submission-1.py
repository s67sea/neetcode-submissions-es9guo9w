from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #O(1)
        self.hm[key].append((timestamp,value)) #tuple of (time,val)
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        #O(log N)
        left = 0
        right = len(self.hm[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            #largst prev value
            if self.hm[key][mid][0] > timestamp:
                #we need to search the first half since timestamps too late
                right = mid - 1
            else:
                #timestamp here <= input timestamp, so we're in the correct half
                #the best answer is either the current one or smth to the right
                #since we want the rightmost
                res = self.hm[key][mid][1]
                left = mid + 1
        return res        

