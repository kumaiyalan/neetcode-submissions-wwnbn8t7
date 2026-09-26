class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def memo(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in cache:
                return cache[n]
            
            res = memo(n - 1) + memo(n - 2)
            cache[n] = res
            return res
            
        return memo(n)