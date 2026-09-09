class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq = 0

        for num in nums_set:
           
            if num-1 not in nums_set:
                curr = num
                streak = 1

                while curr + 1 in nums_set:
                    streak += 1
                    curr += 1

                seq = max(streak, seq)

        return seq

