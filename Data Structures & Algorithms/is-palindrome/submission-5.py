class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        start = 0

        for i in s:
            if i.isalnum():
                res += i.lower()

        end = len(res)-1

        while start <= end:
            
            if res[start] == res[end]:
                start += 1
                end -= 1
            else:
                return False
        return True