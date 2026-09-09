class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        # for i in range(1, len(prices)):
        #     buy = min(buy, prices[i])
        #     profit = prices[i] - buy
        #     res = max(res, profit)


        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            profit = prices[i] - buy
            res = max(profit, res)

        return res