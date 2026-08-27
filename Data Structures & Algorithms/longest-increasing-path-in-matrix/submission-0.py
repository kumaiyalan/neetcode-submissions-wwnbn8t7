class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def memo(r, c, prev):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev):
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            longest = 0
            longest = max(longest, 1 + memo(r + 1, c, matrix[r][c]))
            longest = max(longest, 1 + memo(r - 1, c, matrix[r][c]))
            longest = max(longest, 1 + memo(r, c + 1, matrix[r][c]))
            longest = max(longest, 1 + memo(r, c - 1, matrix[r][c]))
            cache[(r, c)] = longest
            return longest
        
        for i in range(ROWS):
            for j in range(COLS):
                memo(i, j, -1)
        
        return max(cache.values())