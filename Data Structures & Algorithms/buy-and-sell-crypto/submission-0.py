class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_profit = 0

        n = len(prices)

        for i in range(n):
            p = prices[i]

            if p < min_price:
                min_price = p

            profit = p - min_price

            if profit > max_profit:
                max_profit = profit


        return max_profit