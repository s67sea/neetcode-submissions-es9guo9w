class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #the stack is guaranteed to be in non-increasing order
        #entry in the stack is the index of the queued temp
        n = len(temperatures)

        stack = []
        res = [0]*n

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                origindex = stack.pop()
                timetaken = i - origindex
                res[origindex] = timetaken
            
            stack.append(i)
        
        return res