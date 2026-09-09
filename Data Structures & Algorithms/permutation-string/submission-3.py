class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        end = len(s1)
        for i in range(len(s2)-len(s1)+1):
            if sorted(s2[i: end]) == sorted(s1):
                return True
            end += 1 
        
        return False



