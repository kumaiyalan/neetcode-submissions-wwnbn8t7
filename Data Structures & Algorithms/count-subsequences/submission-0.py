class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def memo(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            ways = 0
            # 2 choices, skip or take the curr char if it matches
            if s[i] == t[j]:
                ways += memo(i + 1, j + 1)
            ways += memo(i + 1, j)

            cache[(i, j)] = ways
            return ways
        
        return memo(0, 0)