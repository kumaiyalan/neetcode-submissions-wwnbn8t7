class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(amount, index):
            if amount == 0:
                return 1
            if index >= len(coins):
                return 0
            if (amount, index) in memo:
                return memo[(amount, index)]
            
            #2 choices, include or dont
            include = 0
            if amount - coins[index] >= 0: 
                include = dp(amount - coins[index], index)
            exclude = dp(amount, index + 1)
            memo[(amount, index)] = include + exclude
            return memo[(amount, index)]

        return dp(amount, 0)