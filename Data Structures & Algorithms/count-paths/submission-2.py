class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        cache[(m - 1, n - 1)] = 1

        def memo(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i >= m or j >= n:
                return 0
            
            right = memo(i + 1, j)
            down = memo(i, j + 1)
            cache[(i, j)] = right + down
            
            return right + down
        
        return memo(0, 0)