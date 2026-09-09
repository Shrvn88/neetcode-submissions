class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1

        l = []
        for key, val in hmap.items():
            l.append([val, key])

        l.sort()

        res = []

        while len(res) < k:
            res.append(l.pop()[1])
        
        return res