class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        m1 = [0] * 26
        m2 = [0] * 26

        for c in s1:
            m1[ord(c) - ord('a')] += 1
        l = 0
        for r in range(n):
            m2[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) > m:
                m2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if m1 == m2:
                return True
     
        return False


