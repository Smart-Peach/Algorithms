class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        prev = prices[0]

        for pres_price in prices:

            if pres_price > prev:
                profit += pres_price - prev

            prev = pres_price

        return profit
