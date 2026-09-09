class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        res = 0
        maxF = 0
        l = 0

        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            maxF = max(maxF, hmap[s[r]])

            while (r - l + 1) - maxF > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
            