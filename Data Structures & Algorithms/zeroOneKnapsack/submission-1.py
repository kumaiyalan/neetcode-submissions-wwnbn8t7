class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}

        def dp(capacity, index):
            if capacity <= 0 or index >= len(profit):
                return 0
            if (capacity, index) in memo:
                return memo[capacity, index]

            if capacity - weight[index] >= 0:
                memo[(capacity, index)] = max(dp(capacity, index + 1),
                        profit[index] + dp(capacity - weight[index],   index + 1))
            else:
                memo[(capacity, index)] = dp(capacity, index + 1)
            return memo[(capacity, index)]
        
        return dp(capacity, 0)
