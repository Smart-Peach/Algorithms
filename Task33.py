class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices) - 1:

            while i < len(prices) - 1 and (prices[i + 1] <= prices[i]):
                i += 1
            buy = prices[i]

            while i < len(prices) - 1 and (prices[i + 1] > prices[i]):
                i += 1
            sell = prices[i]
            profit += sell - buy

        return profit
