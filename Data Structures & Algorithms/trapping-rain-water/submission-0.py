class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            l = max(height[:i+1])
            r = max(height[i:])
            val = min(l, r)
            ans = val - height[i]
            res += max(0, ans)
        return res