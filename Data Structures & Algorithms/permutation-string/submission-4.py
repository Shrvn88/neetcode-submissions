class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        end = len(s1)
        m1 = [0] * 26
        for c in s1:
            m1[ord(c)-ord('a')] += 1
        print(m1)
        for i in range(len(s2)-len(s1)+1):
            sub = s2[i: end]
            m2 = [0] * 26
            for c in sub:
                m2[ord(c)-ord('a')] += 1
            if m1 == m2:
                return True
            end += 1 
        
        return False



