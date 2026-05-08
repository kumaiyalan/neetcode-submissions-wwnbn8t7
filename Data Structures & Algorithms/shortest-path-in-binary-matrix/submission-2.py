class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        goal = (ROWS - 1, COLS - 1)
        seen = set()
        seen.add((0, 0))
        queue = deque()
        queue.append((0, 0, 1))
        length = 1

        while queue:
            cell = queue.popleft()
            r, c, distance = cell[0], cell[1], cell[2]
            if (r, c) == goal:
                return distance
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                          (1, 1), (-1, 1), (1, -1), (-1, -1)]
            for nr, nc in directions:
                if (r + nr < 0 or c + nc < 0 or 
                    r + nr >= ROWS or c + nc >= COLS or
                    (r + nr, c + nc) in seen or
                    grid[r + nr][c + nc] == 1):
                    continue
                queue.append((r + nr, c + nc, distance + 1))
                seen.add((r + nr, c + nc))
        return -1
