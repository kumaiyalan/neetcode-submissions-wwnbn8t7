class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        seen = set()
        numFresh = 0
        minute = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    numFresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                    seen.add((row, col))
        if numFresh == 0:
            return minute
        
        while queue:
            for i in range(len(queue)):
                cell = queue.popleft()
                r, c = cell[0], cell[1]

                move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for nr, nc in move:
                    if (r + nr < 0 or c + nc < 0 or
                        r + nr >= ROWS or c + nc >= COLS or
                        (r + nr, c + nc) in seen or
                        grid[r + nr][c + nc] == 0 or 
                        grid[r + nr][c + nc] == 2):
                        continue
                    grid[r + nr][c + nc] = 2    
                    queue.append((r + nr, c + nc))
                    seen.add((r + nr, c + nc))
                    numFresh -= 1
                    if numFresh == 0:
                        return minute + 1
            minute += 1
        if numFresh == 0:
            return minute
        else:
            return -1