class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = 0
        R = 0
        while R < len(prices):
            profit = max(profit, prices[R] - prices[L])
            if prices[R] < prices[L]:
                L = R
            R += 1
        return profit
        