class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}

        def dp(capacity, index):
            if capacity == 0 or index >= len(weight):
                return 0
            if (capacity, index) in memo:
                return memo[(capacity, index)]
            
            # dont use item at all
            skip = dp(capacity, index + 1)

            # use item
            use = 0
            if capacity - weight[index] >= 0:
                use = profit[index] + dp(capacity - weight[index], index)

            memo[(capacity, index)] = max(skip, use)
            return memo[(capacity, index)]

        return dp(capacity, 0) 