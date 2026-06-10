class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        available = set(coins)
        if amount in available:
            return 1
        
        for i in range(1, amount + 1):
            smallest = set()
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    smallest.add(1 + dp[i - coin])
            if len(smallest) == 0:
                dp[i] = -1
            else:
                dp[i] = min(smallest)

        return dp[amount]