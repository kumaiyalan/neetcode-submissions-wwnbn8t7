class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))
        distance = 0
        while queue:
            curr = len(queue)
            for i in range(curr):
                r, c = queue.popleft()
                grid[r][c] = distance
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for nr, nc in directions:
                    if ((0 <= r + nr < ROWS) and (0 <= c + nc < COLS) and
                        grid[r + nr][c + nc] != -1 and (r + nr, c + nc) not in seen):
                        queue.append((r + nr, c + nc))
                        seen.add((r + nr, c + nc))

            distance += 1
        