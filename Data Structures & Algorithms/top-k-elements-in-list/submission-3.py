class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} #map elem:freq
        for elem in nums:
            if elem not in map.keys():
                map[elem] = 1
            else:
                map[elem] += 1
        
        return sorted(list(set(nums)), key= lambda x: -map[x])[:k]