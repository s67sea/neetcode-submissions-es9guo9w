from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #order the tasks in order of most to least frequent

        #if the most frequent task appears maxf times with a cooldown period of n, then we need
        #at least (n+1)*(maxf-1) + count(arg maxf)

        #or if there's too many tasks that we need the extra space then we need the number of tasks

        freqmap = defaultdict(int) #O(26 = 1) space
        for task in tasks: #O(N) time
            freqmap[task] += 1
        
        maxf = max(freqmap.values()) #O(26 = 1) time
        maxfreqcount = list(freqmap.values()).count(maxf)

        minAns = (n+1)*(maxf-1) + maxfreqcount
        numTasks = len(tasks)

        return max(minAns, numTasks)
