class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []

        # for i in range(len(nums)):
        #     ans = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         ans *= nums[j]

        #     res.append(ans)
        
        # return res

        n = len(nums)

        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0], suff[n-1] = nums[0], nums[n-1]

        for i in range(1, n):
            pref[i] = nums[i] * pref[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i]
        for i in range(n):
            res[i] = (1 if i == 0 else pref[i-1]) * (1 if i == n - 1 else suff[i+1])

        return res
        






