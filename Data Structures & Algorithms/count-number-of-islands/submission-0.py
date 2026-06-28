class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            for nr, nc in directions:
                dfs(r + nr, c + nc)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != "0":
                    res += 1
                    dfs(i, j)

        return res