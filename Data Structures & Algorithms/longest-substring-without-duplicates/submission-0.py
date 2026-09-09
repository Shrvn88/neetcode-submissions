class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        sub = set()
        for c in s:
            while c in sub:
                sub.remove(s[left])
                left += 1
            sub.add(c)
            res = max(res, len(sub))
        return res
            
            