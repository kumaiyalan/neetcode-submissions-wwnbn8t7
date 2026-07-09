class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        for coin in coins:
            cache[coin] = 1
        cache[0] = 0

        def sub(amount):
            if amount in cache:
                return cache[amount]
            ways = []
            for coin in coins:
                if amount - coin >= 0:
                    ways.append(sub(amount - coin))
                    if ways[-1] == -1:
                        ways.pop()
            if ways == []:
                cache[amount] = -1
            else:
                cache[amount] = min(ways) + 1
            return cache[amount]

        res = sub(amount)
        return res

        