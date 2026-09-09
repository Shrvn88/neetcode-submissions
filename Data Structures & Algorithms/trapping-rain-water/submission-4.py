class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        rmax = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i+1])

        for i in range(len(height)):
            l = max(l, height[i])
            r = rmax[i]
            val = min(l, r)
            ans = val - height[i]
            res += max(0, ans)
        return res