class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] > prices[buyDay]:
                profit += prices[i] - prices[buyDay]
                buyDay = i
            if prices[i] < prices[buyDay]:
                buyDay = i
        return profit   